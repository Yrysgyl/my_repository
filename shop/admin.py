from django.contrib import admin
from shop.models import Category, Product, Comment



admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Category)