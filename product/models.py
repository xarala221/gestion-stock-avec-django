from django.db import models

from account.models import CustomUser


class Product(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=13, decimal_places=2)
    logo = models.ImageField(upload_to="logos/")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def all_transactions(self):
        return self.transactions.filter(transaction_type=1)


"""[summary]
Un tableau de deux colons
1- LEs technos que j'ai aborde
2- Niveau d'expertise sur une echelle de 10
"""
