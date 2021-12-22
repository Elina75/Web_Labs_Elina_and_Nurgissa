from django import forms
from .models import Cakes


class ProductForm(forms.ModelForm):
    class Meta:
        model = Cakes
        fields = '__all__'