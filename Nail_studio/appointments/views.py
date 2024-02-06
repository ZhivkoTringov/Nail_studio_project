from django.contrib import messages
from django.contrib.auth import mixins as user_mixins
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import generic as views
from .models import *
from django.urls import reverse_lazy
from .models import Appointment
from .forms import AppointmentForm, EditAppointmentForm

UserModel = get_user_model()


class BookAppointmentView(user_mixins.LoginRequiredMixin, views.View):
    """
    View for booking a new appointment.
    """

    template_name = 'appointments/create_appointment.html'
    success_url = reverse_lazy('index')

    def get(self, request):

        """
        Handle GET request for booking appointment form.
        """

        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        """
        Handle POST request for creating a new appointment.
        """

        form = AppointmentForm(request.POST)
        if form.is_valid():

            chosen_date = form.cleaned_data['date']
            chosen_time = datetime.strptime(form.cleaned_data['time'], '%H:%M').time()
            chosen_manicurist = form.cleaned_data['manicurist']

            if not request.user.profile.first_name or not request.user.profile.last_name or not request.user.profile.phone_number:
                form.add_error(None, 'Моля първо попълнете профила си!')
                return render(request, self.template_name, {'form': form})

            start_datetime = datetime.combine(chosen_date, chosen_time)
            end_datetime = start_datetime + timedelta(minutes=form.cleaned_data['service'].duration)

            overlapping_appointments = Appointment.objects.filter(
                manicurist=chosen_manicurist,
                start_time__lt=end_datetime,
                end_time__gt=start_datetime
            )

            if overlapping_appointments.exists():
                form.add_error(None, 'Часът който искате да запазите вече е зает! Моля изберете друг час!')
            else:
                appointment = Appointment(
                    manicurist=chosen_manicurist,
                    service=form.cleaned_data['service'],
                    booked_by=request.user.profile.first_name,
                    start_time=start_datetime,
                    end_time=end_datetime
                )

                appointment.save()

                template = render_to_string('email/appointment_booking_confirmation.html', {
                    'name': request.user.profile.first_name,
                    "service": form.cleaned_data['service'],
                    "date": appointment.start_time
                })
                email = EmailMessage(
                    'Благодарим Ви, че избрахте Краси Нейлс',
                    template,
                    settings.EMAIL_HOST_USER,
                    [request.user.email],
                )
                email.fail_silently = True
                email.send()
                return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class BookedAppointmentsView(user_mixins.LoginRequiredMixin, views.ListView):
    """
    View to display booked appointments for the logged-in user.

    This view displays a list of appointments that have been booked by the currently logged-in user.
    """

    model = Appointment
    template_name = 'appointments/booked_appointments.html'
    context_object_name = 'booked_appointments'

    def get_queryset(self):
        """
        Retrieve and return the queryset of booked appointments by the current user.
        """

        return Appointment.objects.filter(booked_by=self.request.user.profile.first_name)


class ManicuristAppointmentsListView(user_mixins.LoginRequiredMixin, views.ListView):
    """
     View for displaying appointments of a manicurist.

    This view displays a list of appointments for a manicurist if the logged-in user is a manicurist.
    If the user is not a manicurist, no appointments will be displayed.
    """

    template_name = 'appointments/manicurist_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):

        """
        Retrieve and return the queryset of appointments for the current manicurist.
        """

        if UserModel.is_manicurist:
            return Appointment.objects.filter(manicurist=self.request.user).order_by('start_time')
        else:
            return Appointment.objects.none()


class EditAppointmentView(views.UpdateView):
    """
    View for editing an appointment.

    This view allows a manicurist to edit the details of an appointment they are assigned to.
    """

    model = Appointment
    form_class = EditAppointmentForm
    template_name = 'appointments/edit_appointment.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        """
            Retrieve and return the queryset of appointments for the current manicurist.
        """

        return Appointment.objects.filter(manicurist=self.request.user)

    def get_form_kwargs(self):
        """
            Get additional keyword arguments to pass to the form during initialization.
        """

        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs


class DeleteAppointmentView(user_mixins.LoginRequiredMixin, views.DeleteView):
    """
    View for deleting an appointment.

    This view allows a manicurist or admin to delete an appointment.
    """

    model = Appointment
    template_name = 'appointments/delete_appointment.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        """
         Check permissions before dispatching the view.

        :param request: The HTTP request.
        :return: The response or error message
        """

        if not request.user.is_manicurist and not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete the appointment.

        :param request: The HTTP request.
        :return: The response or error message.
        """

        # Add any additional logic if needed
        return super().delete(request, *args, **kwargs)
