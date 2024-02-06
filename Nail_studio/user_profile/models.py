from django.contrib.auth import get_user_model
from django.core import validators, exceptions
from django.db import models

UserModel = get_user_model()


def validate_phone(value):
    cleaned_number = ''.join(filter(str.isdigit, value))

    if len(cleaned_number) != 10:
        raise exceptions.ValidationError('Номерът трябва да съдържа 10 цифри!')

    valid_area_codes = ['087', '088', '089', '098']
    if not cleaned_number.startswith(tuple(valid_area_codes)):
        raise exceptions.ValidationError('Невалиден номер!')


def validate_isalpha(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Трябва да съдържа само букви!')


class Profile(models.Model):
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_NAME = 30

    first_name = models.CharField(

        max_length=MAX_LENGTH_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_NAME),
                    validate_isalpha,
                    ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(

        max_length=MAX_LENGTH_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_NAME),
                    validate_isalpha,
                    ),
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        validators=(validate_phone,),
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def save(self, *args, **kwargs):
        if not self.pk and self.user:
            profile = Profile.objects.create(user=self.user)
            self.pk = profile.pk

        super(Profile, self).save(*args, **kwargs)