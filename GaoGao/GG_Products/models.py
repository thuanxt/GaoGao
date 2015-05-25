from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Category
@python_2_unicode_compatible
class Category(models.Model):
    cate_parent_id = models.ForeignKey('self', null=True, blank=True) # ID of the Parent Category, 0 is no parent
    cate_name = models.CharField(max_length=255) # Category name
    
    # Override __str__ method
    def __str__(self):
        return self.cate_name # Return category name

# Brand
@python_2_unicode_compatible
class Brand(models.Model):
    brand_name = models.CharField(max_length=255) # Brand name
    
    # Override __str__ method
    def __str__(self):
        return self.brand_name # Return brand name

# Product
@python_2_unicode_compatible
class Product(models.Model):
    cate_detail_id = models.ForeignKey(Category) # Category detail ID
    product_name = models.CharField(max_length=255) # Product name
    brand_id = models.ForeignKey(Brand) # Brand ID
    image_url = models.CharField(max_length=255) # Image location
    quantity = models.IntegerField(default=1) # Quantity
    note = models.CharField(max_length=255) # Product note
    description = models.TextField() # Product description
    is_event = models.BooleanField(default=False) # Product is in event or not
    
    # Override __str__ method
    def __str__(self):
        return self.product_name # Return product name
    
# Location
@python_2_unicode_compatible
class Location(models.Model):
    loc_name = models.CharField(max_length=255) # Location name
    
    # Override __str__ method
    def __str__(self):
        return self.loc_name # Return location name
    
# Color
@python_2_unicode_compatible
class Color(models.Model):
    color_name = models.CharField(max_length=255) # Color of the product
    
    # Override __str__ method
    def __str__(self):
        return self.color_name # Return color name
    
# Product Detail
@python_2_unicode_compatible
class ProductDetail(models.Model):
    product_id = models.ForeignKey(Product) # Product ID
    color_id = models.ForeignKey(Color) # Color ID
    loc_id = models.ForeignKey(Location) # Location ID
    quantity = models.IntegerField(default=1) # Quantity
    price = models.DecimalField(max_digits=13, decimal_places=0) # Product price
    
    # Override __str__ method
    def __str__(self):
        return Product.objects.get(pk=self.product_id).product_name # Return product name
    
    class Meta:
        unique_together = ('product_id', 'color_id', 'loc_id')
    
        
