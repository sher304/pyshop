from django.contrib import admin

from .models import Product, Category

admin.site.register(Category)
admin.site.register(Product)

#TODO: Создать категории Smartphones(Samsung, Iphone, Xiaomi),
# Laptops(MacBook, ASUS, Lenovo, Acer), Earphones
