from django import forms
from django.utils import timezone
from datetime import timedelta, datetime
from Nail_studio.services.models import Service
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AppointmentForm(forms.Form):
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
        print(self.fields['time'].choices)

    def get_available_times(self):
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
        cleaned_data = super().clean()
        chosen_date = cleaned_data.get('date')
        chosen_time = cleaned_data.get('time')
        chosen_manicurist = cleaned_data.get('manicurist')
        service_duration = cleaned_data.get('service').duration
        chosen_time = datetime.strptime(cleaned_data.get('time'), '%H:%M').time()
        start_datetime = datetime.combine(chosen_date, chosen_time)
        end_datetime = start_datetime + timedelta(minutes=service_duration)
        return cleaned_data


