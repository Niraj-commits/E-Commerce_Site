from django.shortcuts import render,HttpResponse
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *


def index(request):
    items = Item.objects.filter(is_sold = False)
    category = Category.objects.all()
    context = {
        "total_items":items,
        "categories":category
    }
    
    
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def item_detail(request,pk):
    
    item = Item.objects.get(pk = pk)
    related_items = Item.objects.filter(category = item.category,is_sold=False).exclude(pk = pk)[0:3]
    
    context = {'single_item':item,'related_items':related_items}
    
    return render(request,'items/detail.html',context)

@login_required
def NewItemCreate(request):
    form = NewItemForm()
    
    context = {"new_item":form}
    
    return render(request,'items/create.html',context)