from django.contrib import admin

from Nail_studio.appointments.models import Appointment


@admin.register(Appointment)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('manicurist', 'service', 'start_time', 'end_time')
    search_fields = ('manicurist__username', 'service__name', 'booked_by__username')
    list_filter = ('manicurist', 'service', 'start_time')
    date_hierarchy = 'start_time'

