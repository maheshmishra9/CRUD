from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=155)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    item_id = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="inventory/item", null=True, blank=True)
    model_number = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    remarks = models.TextField()

    def __str__(self):
        return self.name

    
# def generate_category_id(name, id):
#     unique_str = "".join(list(set(name.upper().replace(" ", "")))[:4])
#     user_code = "".join([initials[0] for initials in name.split()]).upper()
#     return "ASP-" + unique_str + "-" + str(id) + user_code

# @receiver(post_save, sender=Category)
# def create_order_code(sender, instance, created, **kwargs):
#     if created:
#         instance.order_id = generate_category_id(
#             instance.user.full_name,
#             instance.pk,
#         )
#         instance.save()

