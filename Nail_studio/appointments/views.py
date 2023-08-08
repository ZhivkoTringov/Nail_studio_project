from django.contrib.auth import mixins as user_mixins
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import generic as views
from .models import *
from django.urls import reverse_lazy
from .models import Appointment
from .forms import AppointmentForm

UserModel = get_user_model()


class BookAppointmentView(views.View):
    template_name = 'appointments/create_appointment.html'
    success_url = reverse_lazy('index')  # Replace with your actual success URL

    def get(self, request):
        form = AppointmentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            chosen_date = form.cleaned_data['date']
            chosen_time = datetime.strptime(form.cleaned_data['time'], '%H:%M').time()
            chosen_manicurist = form.cleaned_data['manicurist']

            start_datetime = datetime.combine(chosen_date, chosen_time)
            end_datetime = start_datetime + timedelta(minutes=form.cleaned_data['service'].duration)

            overlapping_appointments = Appointment.objects.filter(
                manicurist=chosen_manicurist,
                start_time__lt=end_datetime,
                end_time__gt=start_datetime
            )

            if overlapping_appointments.exists():
                form.add_error(None, 'The hours you chose are already taken.')
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
    model = Appointment
    template_name = 'booked_appointments.html'
    context_object_name = 'booked_appointments'


class ManicuristAppointmentsListView(views.ListView):
    template_name = 'manicurist_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        if UserModel.is_manicurist:
            return Appointment.objects.filter(manicurist=self.request.user)
        else:
            # Return an empty queryset for non-manicurist users
            return Appointment.objects.none()