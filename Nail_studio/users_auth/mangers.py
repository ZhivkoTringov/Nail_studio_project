from django.contrib.auth.hashers import make_password
from django.contrib.auth import models as user_models


class AppUserManager(user_models.BaseUserManager):
    """
    Custom user manager for the AppUser model.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        """
        Create and save a user with the given email and password.

        :param email: The user's email address.
        :param password: The user's password.
        :return: The created user object.
        :raises ValueError: If the email is not provided.
        """

        if not email:
            raise ValueError("The given email must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):

        """
        Create a standard user with the given email and password.

        :param email: The user's email address.
        :param password: The user's password.
        :param extra_fields: Any additional fields to set on the user model.
        :return: The created user object.
        """

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):

        """
        Create a superuser with the given email and password.

        :param email: The superuser's email address.
        :param password: The superuser's password.
        :param extra_fields: Any additional fields to set on the user model.
        :return: The created superuser object.
        :raises ValueError: If is_staff or is_superuser fields are not explicitly set to True.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
