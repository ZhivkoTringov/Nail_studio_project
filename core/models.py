from django.core import exceptions
from django.db import models

def validate_isalpha(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Fruit name should contain only letters!')


class Service(models.Model):
    MAX_LENGTH_NAME = 100
    MAX_DIGITS_PRICE = 5
    MAX_DECIMAL_PLACES = 2

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    price = models.DecimalField(
        max_digits=MAX_DIGITS_PRICE,
        decimal_places=MAX_DECIMAL_PLACES,
        null=False,
        blank=False,
    )

    class Meta:
        permissions = [
            ('manage_services', 'Can manage services'),
        ]

    def __str__(self):
        return self.name
