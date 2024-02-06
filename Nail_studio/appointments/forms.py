from django import forms
from django.utils import timezone
from datetime import timedelta, datetime

from Nail_studio.appointments.models import Appointment, UserModel
from Nail_studio.services.models import Service


class AppointmentForm(forms.Form):
    """
      A form for creating a new appointment.

      This form allows users to book appointments with manicurists for available services.
      Users can select the date, time, manicurist, and service for the appointment.

      Attributes:
          DAYS_AHEAD (int): The number of days ahead for which appointments can be booked.
          TIME_SLOT (timedelta): The time slot for each appointment.
          available_dates (list): A list of available appointment dates.
          start_time (time): The start time for appointments.
          end_time (time): The end time for appointments.
          available_times (list): A list of available appointment times.

      Fields:
          date (DateField): Allows users to select the appointment date.
          manicurist (ModelChoiceField): Allows users to select a manicurist.
          service (ModelChoiceField): Allows users to select a service.
          time (ChoiceField): Allows users to select the appointment time based on availability.

      Methods:
          __init__(): Initializes the form with the available time choices.
          get_available_times(): Calculates and returns available appointment times.
          clean(): Validates and cleans the form data, ensuring a valid appointment.

      """

    DAYS_AHEAD = 30
    TIME_SLOT = timedelta(minutes=15)

    available_dates = [(timezone.now().date() + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(DAYS_AHEAD)]
    start_time = datetime.strptime('10:00', '%H:%M').time()
    end_time = datetime.strptime('18:00', '%H:%M').time()
    available_times = [(start_time + i * TIME_SLOT).strftime('%H:%M') for i in
                       range(int((end_time.hour - start_time.hour) * 60 / TIME_SLOT.seconds))]

    date = forms.DateField(
        widget=forms.Select(choices=[(date, date) for date in available_dates])
    )
    manicurist = forms.ModelChoiceField(
        queryset=UserModel.objects.filter(is_manicurist=True)
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'] = forms.ChoiceField(choices=self.get_available_times())

    def get_available_times(self):
        """
            Calculates and returns available appointment times.

            Returns:
                list: A list of available appointment times.
        """

        start_time = datetime.strptime('10:00', '%H:%M').time()
        end_time = datetime.strptime('18:00', '%H:%M').time()
        TIME_SLOT = timedelta(minutes=15)
        available_times = []

        current_time = start_time
        while current_time <= end_time:
            available_times.append((current_time.strftime('%H:%M'), current_time.strftime('%I:%M %p')))
            current_time = (datetime.combine(datetime.today(), current_time) + TIME_SLOT).time()

        return available_times

    def clean(self):
        """
            Validates and cleans the form data, ensuring a valid appointment.

            Returns:
                dict: A dictionary of cleaned and validated form data.
        """

        cleaned_data = super().clean()
        chosen_date = cleaned_data.get('date')
        chosen_time = cleaned_data.get('time')
        chosen_manicurist = cleaned_data.get('manicurist')
        service_duration = cleaned_data.get('service').duration
        chosen_time = datetime.strptime(cleaned_data.get('time'), '%H:%M').time()
        start_datetime = datetime.combine(chosen_date, chosen_time)
        end_datetime = start_datetime + timedelta(minutes=service_duration)
        return cleaned_data


class EditAppointmentForm(forms.ModelForm):
    """
    A form for editing an existing appointment.

    This form allows users to edit the details of an existing appointment, including
    the manicurist, service, start time, and end time.

    Fields:
        manicurist (ModelChoiceField): Allows users to select a manicurist.
        service (ModelChoiceField): Allows users to select a service.
        start_time (DateTimeField): Allows users to modify the appointment start time.
        end_time (DateTimeField): Allows users to modify the appointment end time.

    """

    class Meta:
        model = Appointment
        fields = ['manicurist', 'service', 'start_time', 'end_time']
