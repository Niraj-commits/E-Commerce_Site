from django.db import models
from core.models import MyUser

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=50,default="Items")
    created_by = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    
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
    created_by = models.ForeignKey(MyUser,related_name='items',on_delete=models.CASCADE,default=None)
    created_at = models.DateField( auto_now_add=True)
    quantity = models.IntegerField(default=0)
        
    def __str__(self):
        return self.name
    