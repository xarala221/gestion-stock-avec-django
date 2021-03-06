# Generated by Django 3.2 on 2021-04-28 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_quantity'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[(0, 'Dépense'), (1, 'Revenu')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='product.product'),
        ),
    ]
