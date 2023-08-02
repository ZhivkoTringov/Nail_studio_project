from django.contrib.auth import mixins as user_mixins
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.views import generic as views
from .forms import AppointmentForm
from .models import *
from django.contrib import messages
from ..user_profile.models import Profile

UserModel = get_user_model()


def validWeekday(days):
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y != 'Sunday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def booking(request):
    weekdays = validWeekday(31)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user
            appointment.manicurist = form.cleaned_data['manicurist']

            # Get the selected service duration
            service = form.cleaned_data['service']
            service_duration = service.duration
            # Calculate the end time of the appointment
            appointment_start_time = form.cleaned_data['start_time']
            appointment_end_time = appointment_start_time + timedelta(minutes=service_duration)
            appointment.end_time = appointment_end_time

            # Get the related Profile of the user who booked the appointment
            try:
                profile = Profile.objects.get(user=request.user)
                appointment.booked_by = profile.first_name
            except Profile.DoesNotExist:
                pass  # Handle the case where the Profile doesn't exist for the user

            appointment.save()
            messages.success(request, "Appointment Saved!")
            return redirect('index')
    else:
        form = AppointmentForm()

    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'form': form,
    })


def bookingSubmit(request):
    user = request.user
    times = [
        "10:30", "11:30", "12:30", "13:30", "14:30", "15:30", "16:30", "17:30", "18:30"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')

    # Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)

    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service:
            if minDate <= day <= maxDate:
                if date in ['Monday', 'Saturday', 'Wednesday']:
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            appointment = Appointment.objects.create(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Appointment Saved!")
                            return redirect('index')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return render(request, 'bookingSubmit.html', {
        'times': hour,
    })


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