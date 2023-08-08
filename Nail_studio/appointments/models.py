from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from Nail_studio.services.models import Service
from django.db import models

UserModel = get_user_model()


class Appointment(models.Model):
    time_ordered = models.DateTimeField(default=datetime.now, blank=False)
    manicurist = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        limit_choices_to={'is_manicurist': True},
        related_name='booked_appointments'
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    booked_by = models.CharField(
        max_length=150,
        blank=True,
        editable=False,
    )
    start_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    end_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.start_time or not self.end_time:
            self.start_time = self.calculate_start_time()
            self.end_time = self.start_time + timedelta(minutes=self.service.duration)
        super(Appointment, self).save(*args, **kwargs)

    def calculate_start_time(self):
        return datetime.combine(self.date, self.time)

    def is_time_slot_available(self):
        overlapping_appointments = Appointment.objects.filter(
            manicurist=self.manicurist,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(pk=self.pk if self.pk else None)

        return not overlapping_appointments.exists()

    def __str__(self):
        return f"Appointment: {self.start_time} - {self.end_time}, Manicurist: {self.manicurist}, Service: {self.service}"