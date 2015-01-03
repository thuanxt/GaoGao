from django.db import models

# Category
class Category(models.Model):
    cate_name = models.CharField(max_length=255) # Category name

# Category details
class CategoryDetail(models.Model):
    cate_id = models.ForeignKey(Category) # Category ID
    cate_detail_name = models.CharField(max_length=255) # Category detail name

# Brand
class Brand(models.Model):
    brand_name = models.CharField(max_length=255) # Brand name
    
# Product
class Product(models.Model):
    cate_detail_id = models.ForeignKey(CategoryDetail) # Category detail ID
    brand_id = models.ForeignKey(Brand) # Brand ID
    image_url = models.CharField(max_length=255) # Image location
    quantity = models.IntegerField(default=1) # Quantity
    note = models.CharField(max_length=255) # Product note
    description = models.TextField() # Product description
    is_event = models.BooleanField(default=False) # Product is in event or not
    
# Location
class Location(models.Model):
    loc_name = models.CharField(max_length=255) # Location name
    
# Color
class Color(models.Model):
    color_name = models.CharField(max_length=255) # Color of the product
    
# Product Detail
class ProductDetail(models.Model):
    product_id = models.ForeignKey(Product) # Product ID
    color_id = models.ForeignKey(Color) # Color ID
    loc_id = models.ForeignKey(Location) # Location ID
    quantity = models.IntegerField(default=1) # Quantity
    price = models.DecimalField(max_digits=13, decimal_places=0) # Product price
    
    class Meta:
        unique_together = ('product_id', 'color_id', 'loc_id')
    
        
