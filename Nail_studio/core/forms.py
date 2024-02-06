from django import forms

from Nail_studio.core.models import GalleryPhoto


class ContactForm(forms.Form):
    """
      A Django Form for collecting contact information from users.
      This form includes fields for the user's name, email address, and a message.
    """

    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class GalleryPhotoForm(forms.ModelForm):

    """
     This form is used to interact with the GalleryPhoto model. It includes fields
    for all model fields defined in the GalleryPhoto model.
    """

    class Meta:

        """
         Metaclass specifying the associated model for the form.
        Attributes:
            - model (Model): The model associated with this form (GalleryPhoto).
        """

        model = GalleryPhoto
        fields = "__all__"
