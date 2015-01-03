from django.db import models

# Create your models here.
class Category(models.Model):
    cateName = models.CharField(max_length=200)
    
class CategoryDetail(models.Model):
    cateId = models.ForeignKey(Category)
    cateDetailName = models.CharField(max_length=200)