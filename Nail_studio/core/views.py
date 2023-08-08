from django.views import generic as views


class IndexView(views.TemplateView):
    template_name = 'Index.html'

class AboutView(views.TemplateView):
    template_name = 'About.html'

class ContactUsView(views.TemplateView):
    template_name = 'Contact.html'
