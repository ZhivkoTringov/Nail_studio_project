from django import forms
from django.contrib.auth import views as user_views, login, get_user_model
from django.contrib.auth import forms as user_forms
from django.urls import reverse_lazy
from django.views import generic as views

UserModel = get_user_model()


class RegisterUserForm(user_forms.UserCreationForm):


    class Meta(user_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    consent = forms.BooleanField()


class RegisterUserView(views.CreateView):
    template_name = 'users_auth_templates/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result



class LoginUserView(user_views.LoginView):
    template_name = 'Login-Template.html'




class LogoutUserView(user_views.LogoutView):
    pass
