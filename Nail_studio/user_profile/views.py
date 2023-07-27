from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

UserModel = get_user_model

class ProfileDetailsView(views.DetailView):
    template_name = 'users_profile/profile_details.html'
    model = UserModel

class ProfileEditView(views.UpdateView):
    template_name = 'users_profile/profile_edit.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'users_profile/profile_delete.html'

