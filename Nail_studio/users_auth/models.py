from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import models as user_models

from Nail_studio.users_auth.mangers import AppUserManager


class AppUser(user_models.AbstractBaseUser, user_models.PermissionsMixin):
    USERNAME_FIELD = "email"

    objects = AppUserManager()

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_manicurist = models.BooleanField(
        default=False,
    )