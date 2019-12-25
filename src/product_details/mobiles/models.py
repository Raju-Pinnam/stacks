from django.db.models.signals import post_save, pre_save
from django.db import models

from products.models import Product
from category_sub.models import Category, SubCategory
from product_details.utils import (post_save_details_save_data_to_product_model,
                                   pre_save_slug_generator, upload_image_path)


class Mobile(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)
    color = models.CharField(max_length=120)
    ram = models.FloatField(max_length=120, blank=True, null=True, default=1.0)
    description = models.TextField(blank=True, null=True)

    main_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    left_side_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    right_side_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    back_side_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    is_upcoming = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product_name)


pre_save.connect(pre_save_slug_generator, sender=Mobile)

post_save.connect(post_save_details_save_data_to_product_model, sender=Mobile)
