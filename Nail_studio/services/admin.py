from django.contrib import admin

from Nail_studio.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'categories')
    list_filter = ('categories',)
    search_fields = ('name',)

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'price', 'categories'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'price', 'categories'),
        }),
    )

    ordering = ('name',)
