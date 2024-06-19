# Generated by Django 5.0.6 on 2024-06-17 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_order_status_alter_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.delivery_address', verbose_name='Адрес Доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.TextField(default='SBP', verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='products',
            name='orders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Пользователь'),
        ),
    ]
