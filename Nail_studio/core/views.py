from django.contrib.auth import mixins as auth_mixins
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.conf import settings

from Nail_studio.core.forms import ContactForm, GalleryPhotoForm
from Nail_studio.core.models import GalleryPhoto


class IndexView(views.TemplateView):
    template_name = 'core/Index.html'


class AboutView(views.TemplateView):
    template_name = 'core/About.html'


class ContactView(views.View):
    """
    View for handling contact form submission.

    This view allows users to submit a contact form.

    Attributes:
    - template_name: The name of the template to render.
    - success_url: The URL to redirect to after successful form submission.

    """

    template_name = 'core/Contact.html'
    success_url = reverse_lazy('index')

    def get(self, request):
        """
        Handle GET request for the contact form.

        :param request: The HTTP request.
        :return: The rendered template with an empty contact form.
        """

        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Handle POST request for the contact form.

        :param request: The HTTP request.
        :return: Redirect to success_url or render template with errors.
        """

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


class GalleryView(views.View):
    """
    View for displaying the photo gallery.

    This view displays a gallery of photos.

    Attributes:
    - template_name: The name of the template to render.
    """

    template_name = 'gallery/photo_gallery.html'

    def get(self, request):
        """
        Handle GET request for displaying the photo gallery.

        :param request: The HTTP request.
        :return: The rendered template with the list of photos.
        """

        photos = GalleryPhoto.objects.all()
        return render(request, self.template_name, {'photos': photos})


class UploadPhotoView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    """
    View for uploading a photo to the gallery.

    This view allows authorized users to upload photos to the gallery.
    """

    model = GalleryPhoto
    form_class = GalleryPhotoForm
    template_name = 'gallery/upload_photo.html'
    permission_required = 'phtogallery.manage_photos'
    success_url = reverse_lazy('gallery')


class DeletePhotoView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    """
    View for deleting a photo from the gallery.

    This view allows authorized users to delete photos from the gallery.
    """

    model = GalleryPhoto
    template_name = 'gallery/delete_photo.html'
    permission_required = 'phtogallery.manage_photos'
    success_url = reverse_lazy('gallery')  # Redirect after successful deletion

    def get_context_data(self, **kwargs):
        """
        Get additional context data to pass to the template.
        """

        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Photo'
        return context


def custom_404(request, exception):

    """
    Custom view for rendering the 404 error page.

    :param request: The HTTP request.
    :param exception: The exception that triggered the 404 error.
    :return: The rendered template for the 404 error page.
    """
    return render(request, '404_page/404-Not-Found-Template.html', status=404)
