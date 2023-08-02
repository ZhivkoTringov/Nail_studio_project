from datetime import timedelta

from django import forms
from django.contrib.auth import get_user_model
from .models import Appointment
from .utils import is_time_slot_available

UserModel = get_user_model()

class AppointmentForm(forms.ModelForm):
    manicurist = forms.ModelChoiceField(
        queryset=UserModel.objects.filter(is_manicurist=True),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        input_formats=["%Y-%m-%dT%H:%M"],  # Format to parse the input from the DateTimeInput
    )

    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time', 'manicurist', 'start_time',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.manicurist:
            self.fields['manicurist'].initial = self.instance.manicurist
            self.fields['manicurist'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        service = cleaned_data.get('service')

        if start_time and service:
            # Get the service duration in minutes
            service_duration = service.duration

            # Calculate the end time of the appointment
            end_time = start_time + timedelta(minutes=service_duration)

            # Check availability and update the is_available field
            if not is_time_slot_available(cleaned_data['day'], start_time, end_time):
                raise forms.ValidationError("This time slot is not available.")

            cleaned_data['is_available'] = True  # Update availability

        return cleaned_data
