# Generated by Django 3.0.1 on 2019-12-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=0.0, max_length=120),
        ),
    ]