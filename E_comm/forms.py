from django import forms
from .models import *

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','image','category']