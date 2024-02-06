from django import forms
from Nail_studio.services.models import Service


class BaseServiceForm(forms.ModelForm):
    """
    Base form for Service model.

    This form is used as a base for creating, editing, and deleting Service instances.
    """

    class Meta:

        """
        Meta (class): Configuration options for the form.
        """

        model = Service
        labels = {

            'name': '',
            'price': ''
        }
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Име на услугата'}),
            'price': forms.TextInput(attrs={'placeholder': 'Цена на услугата'}),

        }


class CreateServiceForm(BaseServiceForm):
    """
    Form for creating a new Service instance.

    Inherits from BaseServiceForm.
    """

    pass


class EditServiceForm(BaseServiceForm):
    """
    Form for editing an existing Service instance.

    Inherits from BaseServiceForm.
    """

    class Meta:

        """
        Meta (class): Configuration options for the form.
        """

        model = Service
        labels = {
            'name': 'Име на услугата',
            'price': 'Цена на услугата',
        }
        fields = "__all__"


class DeleteServiceForm(EditServiceForm):
    """
     Form for deleting an existing Service instance.

     Inherits from EditServiceForm.

     Attributes:
         __init__ (method): Initializes the form and sets disabled fields.
         save (method): Deletes the associated Service instance.
         __set_disabled_fields (method): Sets all form fields to be disabled.
     """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True
