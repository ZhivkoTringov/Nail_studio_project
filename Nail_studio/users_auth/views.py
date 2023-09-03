from django import forms
from django.contrib.auth import views as user_views, login, get_user_model
from django.contrib.auth import forms as user_forms
from django.urls import reverse_lazy
from django.views import generic as views

UserModel = get_user_model()


class RegisterUserForm(user_forms.UserCreationForm):

    """
    A custom form to register a new user.

    This form is based on Django's built-in UserCreationForm and is designed
    to allow registration using only the 'email' field.
    """

    class Meta(user_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class RegisterUserView(views.CreateView):

    """
    A view for user registration.

    This view allows a user to register with an email address using the
    RegisterUserForm. Upon successful registration, the user is automatically
    logged in and redirected to the 'success_url'.
    """

    template_name = 'users_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        """
        Handle the form submission when it is valid.

        After successfully processing the form submission using the parent class,
        this method logs in the newly registered user and returns the result.
        :param form: The valid form instance.
        :return: The response for the successful registration.
        """

        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(user_views.LoginView):

    """
     A view for user login.

    This view is based on Django's built-in LoginView and uses the default
    behavior for user login.
    """

    template_name = 'users_auth/login.html'


class LogoutUserView(user_views.LogoutView):

    """
    A view for user logout.

    This view is based on Django's built-in LogoutView and uses the default
    behavior for user logout.
    """

    pass
