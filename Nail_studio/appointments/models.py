from django.db import models
class Appointment(models.Model):


    username = models.CharField(
        max_length= 30,
        null=False,
        blank=False,
    )
