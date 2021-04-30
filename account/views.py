from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm
from account.forms import RegisterForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"You are now logged in as {email}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        return render(
            request,
            "account/login.html",
        )


def register_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                login(request, user)
                return redirect('index')
        else:
            form = RegisterForm()
    return render(
        request,
        "account/register.html",
        {"form": form}
    )
