from cProfile import label

from django import forms
from django.forms import models

from django.shortcuts import render

from django.contrib.auth import views as user_views, login
from django.contrib.auth import forms as user_forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views


class RegisterUserForm(user_forms.UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

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
    template_name = 'users_auth_templates/login.html'



class LogoutUserView(views.View):
    pass
