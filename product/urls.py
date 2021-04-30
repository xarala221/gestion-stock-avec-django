from django.urls import path
from .views import edit_product, index, about, contact, all_products, add_product, product_detail, delete_product


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("products/", all_products, name="all_products"),
    path("products/<int:id>/", product_detail, name="product_detail"),
    path("add-product/", add_product, name="add_product"),
    path("products/<int:id>/edit", edit_product, name="edit_product"),
    path("products/<int:id>/delete", delete_product, name="delete_product"),
]
