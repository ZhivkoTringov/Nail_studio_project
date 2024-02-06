from django.apps import AppConfig




class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Nail_studio.user_profile'

    def ready(self):
        import Nail_studio.user_profile.signals
