# Generated by Django 3.0.1 on 2019-12-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0007_mobile_ram'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
