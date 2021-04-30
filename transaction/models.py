from django.db import models


class Transaction(models.Model):
    SPENT = 0
    INCOME = 1
    TRANSACTION_TYPE = [
        (SPENT, "Dépense"),
        (INCOME, "Revenu")
    ]

    transaction_type = models.CharField(
        max_length=1, choices=TRANSACTION_TYPE, default=INCOME)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="transactions", null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.product} : {self.price}"

    def total_price(self):
        return self.quantity * self.price
