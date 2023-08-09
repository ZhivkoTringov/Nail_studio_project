from django.contrib import admin

from Nail_studio.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'categories')  # Customize the list display columns
    list_filter = ('categories',)  # Add a filter for categories
    search_fields = ('name',)  # Add a search field for name

    # Customize the detail view fields
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'price', 'categories'),
        }),
    )

    # Customize the add/edit form layout
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'price', 'categories'),
        }),
    )

    ordering = ('name',)  # Set the default ordering


