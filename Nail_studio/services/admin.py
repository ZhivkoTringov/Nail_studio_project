from django.contrib import admin

from Nail_studio.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass