from django.contrib.auth import mixins as user_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from Nail_studio.user_profile.models import Profile


class ProfileDetailsView(user_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'profile_user/profile_details.html'
    model = Profile


class ProfileEditView(user_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'profile_user/profile_edit.html'
    model = Profile
    fields = ('first_name', 'last_name', 'phone_number',)
    success_url = reverse_lazy('index')


class ProfileDeleteView(user_mixins.LoginRequiredMixin, views.DeleteView):
    model = Profile
    fields = "__all__"
    template_name = 'profile_user/profile_delete.html'
    success_url = reverse_lazy('index')


