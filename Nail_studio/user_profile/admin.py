from django.contrib import admin

from Nail_studio.user_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
