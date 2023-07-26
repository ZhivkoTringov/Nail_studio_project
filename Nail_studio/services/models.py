from django.core import exceptions, validators
from django.db import models


def validate_isalpha(value):
    for ch in value:
        if not ch.isalpha() and not ch.isspace():
            raise exceptions.ValidationError('Трябва да съдържа само букви!')


NAILS = 'Нокти'
EYEBROWS = 'Вежди'
WAXING = 'Кола маска'
FACE = 'Лице'
OTHER_TYPE = 'Други'

CATEGORIES = ((NAILS, NAILS),
         (EYEBROWS, EYEBROWS),
         (WAXING, WAXING),
         (FACE, FACE),
         (OTHER_TYPE, OTHER_TYPE),
         )


class Service(models.Model):
    MAX_LENGTH_NAME = 100
    MAX_DIGITS_PRICE = 5
    MAX_DECIMAL_PLACES = 2
    MAX_LENGTH_CATEGORY = 50

    categories = models.CharField(
        max_length=MAX_LENGTH_CATEGORY,
        choices=CATEGORIES,
        null=False,
        blank=False,
        default=NAILS,
    )

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MaxLengthValidator(MAX_LENGTH_CATEGORY),
            validate_isalpha,
        ),

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
