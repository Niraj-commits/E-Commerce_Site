from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    items = Item.objects.filter(is_sold = False)
    category = Category.objects.all()
    context = {
        "total_items":items,
        "categories":category
    }
    return render(request,'home.html',context)

def contact(request):
    return render(request,'contact.html')

def ViewProduct(request,pk):
    
    item = Item.objects.get(pk = pk)
    related_items = Item.objects.filter(category = item.category,is_sold=False).exclude(pk = pk)[0:3]
    context = {'single_item':item,'related_items':related_items}
    
    return render(request,'items/Products/detail.html',context)

@login_required
def NewProduct(request):
    prev_category = Category.objects.all()
    context = {"category":prev_category}
    
    if request.method == "POST":
        name = request.POST.get('item')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        created_by = request.user
        image = request.FILES.get('image')
        category = Category.objects.get(id = category_id)
        
        Item.objects.create(name = name,category = category,description= description,image= image,price = price,created_by = created_by)
        return redirect('/')
    return render(request,'items/Products/create.html',context)

@login_required
def DeleteProducts(request,pk):
    queryset = Item.objects.get(pk = pk)
    user = request.user
    if queryset.created_by == user:
        queryset.delete()
        return redirect('/')

@login_required
def MyProducts(request):
    user = request.user
    queryset = Item.objects.filter(created_by = user)
    context = {"items":queryset}
    return render(request,'items/Products/myProducts.html',context)

@login_required
def EditProducts(request,pk):
    queryset = Item.objects.get(pk = pk)
    context = {"data":queryset}
    
    if request.method == "POST":
        item = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        queryset.name = item
        queryset.description = description
        queryset.price = price
        
        if image:
            queryset.image = image
        queryset.save()
        return redirect('item_details',pk=queryset.pk)
    
    return render(request,'items/Products/edit.html',context)

@login_required
def NewCategory(request): 
    
    if request.method == "POST":
        category = request.POST.get("category")
        created_by = request.user
        
        Category.objects.create(name = category,created_by = created_by)
        return redirect('/')
        
    return render(request,'items/category/create.html')

@login_required
def ViewCategory(request):
    user = request.user
    queryset = Category.objects.filter(created_by = user)
    context = {"categories":queryset}
    return render(request,'items/category/myCategories.html',context)

@login_required
def EditCategory(request,pk):
    queryset = Category.objects.get(pk = pk)
    context = {"category":queryset}
    
    if request.method == "POST":
        name = request.POST.get('category')
        queryset.name = name
        queryset.save()
        return redirect("MyCategories")
    
    return render(request,"items/category/edit.html",context)

@login_required
def DeleteCategory(request,pk):
    queryset = Category.objects.get(pk = pk)
    
    if Item.objects.filter(category = queryset).exists():
        messages.error(request, "Sorry, this category is in use and cannot be deleted.")
    
    try:
        queryset.delete()
        messages.success(request, "Category deleted successfully.")
    
    except:
        messages.error(request,"Error Occured")
    
    return redirect("MyCategories")