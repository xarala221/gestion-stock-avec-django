from transaction.models import Transaction
from django.contrib import messages
from django.db.models.aggregates import Sum
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from product.forms import NewProductForm

from .models import Product


def about(request):
    return render(request, "product/about.html")


def contact(request):
    return render(request, "product/contact.html")


@login_required(login_url="login")
def index(request):
    owner = request.user
    transaction_spents = Transaction.objects.filter(
        transaction_type=0, product__owner=owner)
    transaction_incomes = Transaction.objects.filter(
        transaction_type=1, product__owner=owner)
    product_count = Product.objects.count()
    expenses = Transaction.objects.filter(
        transaction_type=0, product__owner=owner).aggregate(Sum("price"))["price__sum"]
    incomes = Transaction.objects.filter(
        transaction_type=1, product__owner=owner).aggregate(Sum("price"))["price__sum"]
    sales_figures = incomes - expenses if incomes and expenses else 0
    return render(request, "product/index.html", {"transaction_spents": transaction_spents, "transaction_incomes": transaction_incomes, "product_count": product_count, "sales_figures": sales_figures, "incomes": incomes, "expenses": expenses, })


# Lister tous les produits/services

@login_required
def all_products(request):
    owner = request.user
    products = Product.objects.filter(owner=owner)
    return render(request, "product/all-products.html", {"products": products})


# Afficher le detail d'un service
@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product/product-detail.html", {"product": product})

# Ajouter un nouveau produit/service


@login_required
def add_product(request):
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("all_products")
        else:
            print(form.errors)
            messages.error(request, f"Erreur : {form.errors}")
            return redirect("add_product")
    else:
        form = NewProductForm()
    return render(request, "product/add-prodcut.html", {"form": form})


# Modifier un produit/service
@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect("all_products")
        else:
            messages.error(request, f"Erreur : {form.errors}")
            return redirect("edit_product")
    else:
        form = NewProductForm(instance=product)
    return render(request, "product/edit-prodcut.html", {"form": form})

# Supprimer un produit/service


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("all_products")
    return render(request, "product/delete-product.html", {"product": product})
