from django.contrib import admin
from GG_Products.models import Category, Product, Brand, Location, Color, ProductDetail

# Register your models here.
list_model = [Category, Product, Brand, Location, Color, ProductDetail]
admin.site.register(list_model)
