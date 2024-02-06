from django.contrib import admin

from Nail_studio.users_auth.models import AppUser


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    pass

