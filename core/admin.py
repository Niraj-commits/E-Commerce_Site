from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUser(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password','role','phone_number','address','store_name')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','password','role','phone_number','address','store_name'),
        }),
    )


admin.site.register(MyUser,CustomUser)
