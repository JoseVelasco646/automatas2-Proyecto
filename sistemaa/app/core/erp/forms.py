from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import *
from django.forms.utils import ErrorList
from core.erp.models import Category, Product

class CategoryForm(ModelForm):



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name' : TextInput(
                attrs = {
                    'placeholder' : 'Ingrese una categoria'
                }
            ),
            'desc' : Textarea(
                attrs = {
                    'placeholder' : 'Ingrese una categoria',
                    'rows' : 3,
                    'cols' :3
                }
            ),
        }


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }