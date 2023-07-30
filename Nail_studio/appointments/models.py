import user_profile
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.models import User

from django.db import models
from datetime import datetime

from django.http import request

from Nail_studio.services.models import Service

TIME_CHOICES = (
    ("10:30", "10:30"),
    ("11:30", "11:30"),
    ("12:30", "12:30"),
    ("13:30", "13:30"),
    ("14:30", "14:30"),
    ("15:30", "15:30"),
    ("16:30", "16:30"),
    ("17:30", "17:30"),
    ("18:30", "18:30"),
)


UserModel = get_user_model()



class Appointment(models.Model):
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="10:30")
    time_ordered = models.DateTimeField(default=datetime.now, blank=False)
    manicurist = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        limit_choices_to={'is_manicurist': True},
        related_name='booked_appointments'  # Add a related_name for reverse relationship
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, blank=False)
    # Add a field to store the name of the user who booked the appointment
    booked_by = models.CharField(max_length=150, blank=True, editable=False)

    def __str__(self):
        return f"Appointment on {self.day} at {self.time} by {self.booked_by}"

