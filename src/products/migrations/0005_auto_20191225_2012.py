# Generated by Django 3.0.1 on 2019-12-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]