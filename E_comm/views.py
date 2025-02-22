from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required


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
    print("View function called")
    prev_category = Category.objects.all()
    context = {"category":prev_category}
    
    if request.method == "POST":
        print("Form submitted!") 
        name = request.POST.get('item')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        created_by = request.user
        image = request.FILES.get('image')
        category = Category.objects.get(id = category_id)
        
        Item.objects.create(name = name,category = category,description= description,image= image,price = price,created_by = created_by)
        return redirect('/')
    return render(request,'items/create.html',context)

@login_required
def deleteItem(request,pk):
    queryset = Item.objects.get(pk = pk)
    user = request.user
    if queryset.created_by == user:
        queryset.delete()
        return redirect('/')

@login_required
def myProducts(request):
    user = request.user
    queryset = Item.objects.filter(created_by = user)
    context = {"items":queryset}
    return render(request,'items/user_products.html',context)

@login_required
def editProducts(request,pk):
    queryset = Item.objects.get(pk = pk)
    
    if request.method == "POST":
        item = request.POST.get('item')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = Category.objects.get(id = category_id)
        
        queryset.name = item
        queryset.category = category
        queryset.description = description
        queryset.price = price
        queryset.image = image
        queryset.save()
        return redirect('/')