# Generated by Django 3.0.1 on 2019-12-26 21:04

import cart.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax',
            field=models.FloatField(default=5.0, max_length=120, validators=[cart.utils.validate_tax]),
        ),
    ]
