from product.models import Product
from django import forms
from .models import Transaction


class NewTransactionSpentForm(forms.ModelForm):
    quantity = forms.CharField(
        label="Quantité",
        widget=forms.NumberInput({"class": "form-control"}))
    price = forms.CharField(
        label="Prix",
        widget=forms.NumberInput({"class": "form-control"}))

    class Meta:
        model = Transaction
        fields = ('quantity', 'price',)


class NewTransactionIncomeForm(forms.ModelForm):
    quantity = forms.CharField(
        label="Quantité vendu",
        widget=forms.NumberInput({"class": "form-control"}))
    price = forms.CharField(
        label="Prix vendu",
        widget=forms.NumberInput({"class": "form-control"}))
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), widget=forms.Select({"class": "form-control"}))

    class Meta:
        model = Transaction
        fields = ('product', 'quantity', 'price',)
