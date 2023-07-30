from django import forms
from django.contrib.auth import get_user_model
from .models import Appointment

UserModel = get_user_model()

class AppointmentForm(forms.ModelForm):
    manicurist = forms.ModelChoiceField(
        queryset=UserModel.objects.filter(is_manicurist=True),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time', 'manicurist']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.manicurist:
            self.fields['manicurist'].initial = self.instance.manicurist
            self.fields['manicurist'].widget.attrs['readonly'] = True
