# Generated by Django 5.0.6 on 2024-06-17 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_reservproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product', verbose_name='Продукт'),
        ),
    ]
