from django import forms

from .model import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                'title',
                'description',
                'price'

            ]