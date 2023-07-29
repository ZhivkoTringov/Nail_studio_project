from django.contrib.auth import get_user_model
from django.contrib.messages import success
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from Nail_studio.user_profile.models import Profile


# UserModel = get_user_model

class ProfileDetailsView(views.DetailView):
    template_name = 'users_profile/profile_details.html'
    model = Profile


class ProfileEditView(views.UpdateView):
    template_name = 'users_profile/profile_edit.html'
    model = Profile
    fields = ('first_name', 'last_name', 'phone_number',)
    success_url = reverse_lazy('index')


class ProfileDeleteView(views.DeleteView):
    model = Profile
    fields = "__all__"
    template_name = 'users_profile/profile_delete.html'
    success_url = reverse_lazy('index')


