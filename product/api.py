from product.serailizers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        owner = self.request.user
        return Product.objects.filter(owner=owner)
