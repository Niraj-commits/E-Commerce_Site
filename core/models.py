from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    role_choices = [('seller','seller'),('buyer','buyer')]
    
    role = models.CharField(max_length=10,choices=role_choices,default="buyer")
    store_name = models.CharField(max_length=25,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=25)