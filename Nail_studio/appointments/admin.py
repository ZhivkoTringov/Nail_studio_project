from django.contrib import admin

from Nail_studio.appointments.models import Appointment


@admin.register(Appointment)
class AppointmentsAdmin(admin.ModelAdmin):
    pass

