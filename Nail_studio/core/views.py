
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.conf import settings

from Nail_studio.core.forms import ContactForm


class IndexView(views.TemplateView):
    template_name = 'Index.html'

class AboutView(views.TemplateView):
    template_name = 'About.html'


class ContactView(views.View):
    template_name = 'contact.html'
    success_url = reverse_lazy('index')

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = 'Contact Form Submission'
            message = f'From: {name}\nEmail: {email}\n\n{message}'
            from_email = email
            recipient_list = [settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, recipient_list)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})



