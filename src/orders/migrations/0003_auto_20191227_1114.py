# Generated by Django 3.0.1 on 2019-12-27 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191227_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_total',
            new_name='shipping_charges',
        ),
    ]