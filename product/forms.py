from django import forms
from .models import Product


class NewProductForm(forms.ModelForm):
    name = forms.CharField(
        label="Nom du produit",
        widget=forms.TextInput({"class": "form-control"}))
    quantity = forms.CharField(
        label="Quantité en stock",
        widget=forms.NumberInput({"class": "form-control"}))
    logo = forms.ImageField(
        label="Image du produit",
        widget=forms.FileInput({"class": "form-control"}))
    price = forms.CharField(
        label="Prix",
        widget=forms.NumberInput({"class": "form-control"}))

    class Meta:
        model = Product
        fields = ('name', 'quantity', 'price', 'logo',)
