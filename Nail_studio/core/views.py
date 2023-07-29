from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views




class IndexView(views.TemplateView):
    template_name = 'proba template/site/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = "Welcome to our Nail Studio!"
    #     return context


