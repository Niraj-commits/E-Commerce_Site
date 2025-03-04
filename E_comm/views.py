from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from .filters import ItemFilter

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

# To Check if the user is seller or not
def is_seller(user):
    return user.role == "seller"

def is_buyer(user):
    return user.role == "buyer"

@login_required
@user_passes_test(is_seller)
def NewProduct(request):
    prev_category = Category.objects.all()
    context = {"category":prev_category}
    
    if request.method == "POST":
        name = request.POST.get('item')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        created_by = request.user
        image = request.FILES.get('image')
        category = Category.objects.get(id = category_id)
        
        intQuantity = int(quantity)
        intPrice = int(price)
        if intQuantity >0 and intPrice > 0:
            Item.objects.create(name = name,category = category,description= description,image= image,price = price,quantity = quantity,created_by = created_by)
            messages.success(request,"Product Created!!!")
            return redirect('myProducts')
        else:
            messages.error(request,"Quantity and price Cannot be less than 0")
    return render(request,'items/Products/create.html',context)

@login_required
@user_passes_test(is_seller)
def DeleteProducts(request,pk):
    queryset = Item.objects.get(pk = pk)
    user = request.user
    if queryset.created_by == user:
        queryset.delete()
        return redirect('myProducts')

@login_required
@user_passes_test(is_seller)
def MyProducts(request):
    user = request.user
    Items = Item.objects.filter(created_by = user)
    item_filter = ItemFilter(request.GET, queryset=Items)
    print(item_filter.qs)
    context = {"filter": item_filter}
    return render(request,'items/Products/myProducts.html',context)

@login_required
@user_passes_test(is_seller)
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
        return redirect('myProducts')
    
    return render(request,'items/Products/edit.html',context)

@login_required
@user_passes_test(is_seller)
def NewCategory(request): 
    
    if request.method == "POST":
        category = request.POST.get("category")
        created_by = request.user
        
        Category.objects.create(name = category,created_by = created_by)
        messages.success(request, "Category Created successfully.")
        return redirect('MyCategories')
        
    return render(request,'items/category/create.html')

@login_required
@user_passes_test(is_seller)
def ViewCategory(request):
    user = request.user
    queryset = Category.objects.filter(created_by = user)
    context = {"categories":queryset}
    return render(request,'items/category/myCategories.html',context)

@login_required
@user_passes_test(is_seller)
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
@user_passes_test(is_seller)
def DeleteCategory(request,pk):
    queryset = Category.objects.get(pk = pk)
    occurence = Item.objects.filter(category = queryset).count()
    if occurence>0:
        messages.error(request, "Sorry, this category is in use and cannot be deleted.")
    else:
        queryset.delete()
        messages.success(request, "Category deleted successfully.")
    
    return redirect("MyCategories")

@login_required
@user_passes_test(is_buyer)

def PurchaseDetail(request, pk):
    item = Item.objects.get(pk = pk)
    
    if request.method == "POST":
        got_quantity = request.POST.get("total")
        if got_quantity is not None:
                got_quantity = int(got_quantity)
                if got_quantity > 0:
                    if item.quantity >= got_quantity:
                        item.quantity -= got_quantity
                        item.save()
                        messages.success(request, "You have successfully purchased the item!")
                        return redirect("/")
                    else:
                        messages.error(request, "Not enough stock available.")
                else:
                    messages.error(request, "Quantity must be greater than zero.")
        else:
            messages.error(request,"Field Cannot be empty")
    return render(request, 'items/sell/buy_product.html', {"item": item})

@login_required
@user_passes_test(is_seller)
def AddProducts(request, pk):
    item = Item.objects.get(pk = pk)
    context = {"items":item}
    
    if request.method == "POST":
        got_quantity = request.POST.get("total")
        if got_quantity is not None:
                got_quantity = int(got_quantity)
                if got_quantity > 0:
                    item.quantity += got_quantity
                    item.save()
                    messages.success(request, "You have successfully purchased the item!")
                    return redirect("myProducts")
                else:
                    messages.error(request, "Quantity must be greater than zero.")
        else:
            messages.error(request,"Field Cannot be empty")
    return render(request, 'items/Products/add_product_quantity.html',context)
