from django import forms

from Nail_studio.core.models import Service


class BaseServiceForm(forms.ModelForm):
    class Meta:
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

class CreateFruitForm(BaseServiceForm):
    pass


class EditFruitForm(BaseServiceForm):
    class Meta:
        model = Service
        labels = {
            'name': 'Име на услугата',
            'price': 'Цена на услугата',
        }
        fields = "__all__"


class DeleteFruitForm(EditFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()



    def save(self, commit=True):
        if commit:
            self.instance.delete()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True