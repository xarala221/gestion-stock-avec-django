from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=65, widget=forms.EmailInput({"class": "form-control"}))
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput({"class": "form-control"}))
    password2 = forms.CharField(
        label="Confirmation de Mot de passe",
        widget=forms.PasswordInput({"class": "form-control"}))
    first_name = forms.CharField(
        label="Prénom",
        widget=forms.TextInput({"class": "form-control"}))
    last_name = forms.CharField(
        label="Nom de famille",
        widget=forms.TextInput({"class": "form-control"}))

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2", "first_name", "last_name"]
