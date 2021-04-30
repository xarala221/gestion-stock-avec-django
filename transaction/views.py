from django.contrib.auth.decorators import login_required
from transaction.forms import NewTransactionIncomeForm, NewTransactionSpentForm
from django.shortcuts import redirect, render
from .models import Transaction


@login_required
def all_transactions(request):
    owner = request.user
    transactions = Transaction.objects.filter(product__owner=owner)
    return render(request, "transaction/all-transactions.html", {"transactions": transactions})


@login_required
def add_spent(request):
    if request.method == "POST":
        form = NewTransactionSpentForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.transaction_type = 0
            transaction.save()
            return redirect("all_transactions")
    form = NewTransactionSpentForm()
    return render(request, "transaction/spent.html", {"form": form})


@login_required
def add_income(request):
    if request.method == "POST":
        form = NewTransactionIncomeForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.transaction_type = 1
            transaction.save()
            return redirect("all_transactions")
    form = NewTransactionIncomeForm()
    return render(request, "transaction/income.html", {"form": form})
