from django.contrib import admin

from .models import Category, Brand, Item, Admin


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(Admin)