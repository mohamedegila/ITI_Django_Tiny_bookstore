from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        user  = authenticate(username=username,password=password)
       
        if user:
            login(request,user)
            return redirect('index')
    return render(request,"registration/signup.html",{
        'form' : form
    })