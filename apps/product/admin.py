from django.contrib import admin

from apps.product.models import Category, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)