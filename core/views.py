
from django.shortcuts import render,redirect
from .forms import *

def signup(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')   
    else:
        form = SignupForm()
    context = {"signup":form}
    return render(request,'authentication/signup.html',context)

