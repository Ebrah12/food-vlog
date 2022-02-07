from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,auth

from . forms import RegisterForm
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful.")
        return redirect("/")
    else:
        form=RegisterForm()
    return render(request,"register.html",{"form":form})
def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.info(request,"Invalid details")
        else:
            messages.info(request, "Invalid details")

    form=AuthenticationForm()
    return render(request,"login.html",{"login_form":form})


def logoutu(request):
    logout(request)
    messages.info(request,"You have successfully logged out.")
    return redirect("/")






