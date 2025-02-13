from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=50,default="Items")
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50,default=None)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="items",default=None)
    image = models.ImageField(upload_to="Prod_Images",null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=50)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE,default=None)
    created_at = models.DateTimeField( auto_now_add=True)
    
        
    def __str__(self):
        return self.name