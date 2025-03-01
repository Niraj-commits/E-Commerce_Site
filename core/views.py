
from django.shortcuts import render,redirect
from .models import *
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages

def RegisterSeller(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        store_name = request.POST.get('store_name')
        address = request.POST.get('address')
        password = request.POST.get('password')
        role = "seller"
        hashed_password = make_password(password)
        
        MyUser.objects.create(username = username,email=email,phone_number = phone,address = address,store_name = store_name,password = hashed_password,role = role)
        
        return redirect("login")
    return render(request,"authentication/register_seller.html")

def RegisterBuyer(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        role = "buyer"
        hashed_password = make_password(password)
        
        MyUser.objects.create(username = username,email=email,phone_number = phone,address = address,password = hashed_password,role = role)
        
        return redirect("login")
    return render(request,"authentication/register_buyer.html")

def CustomLogin(request):
    
    if request.user.is_authenticated:
        if request.user.role == "seller":
            return redirect('/')
        elif request.user.role == "buyer":
            return redirect("/")
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")

        user = authenticate(request,username = username,password= password)
        if user:
            login(request,user)

            if user.role == 'seller':
                return redirect('/')
            elif user.role == 'buyer':
                return redirect('buyer_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('custom_login')
    return render(request,"authentication/login.html")
        
def logout(request):
    auth.logout(request)
    messages.success(request,"Log out successful")
    return redirect("/")