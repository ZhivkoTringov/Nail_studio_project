from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):

    """
    Signal handler function to create a user profile when a new user is created.

    :param sender: The sender of the signal (UserModel).
    :param instance: The user instance that was created.
    :param created: A boolean indicating if the user was just created.
    """

    if created:
        Profile.objects.create(user=instance)


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    """
    Signal handler function to delete a user when their associated profile is deleted.

    :param sender: The sender of the signal (Profile).
    :param instance: The profile instance that was deleted.
    """

    try:
        user = UserModel.objects.get(pk=instance.user_id)
        user.delete()
    except UserModel.DoesNotExist:
        pass
