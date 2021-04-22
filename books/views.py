from django.shortcuts import render,redirect
from .forms import BookForm
from django.http import HttpResponse
from .models import Book
from django.db.models import Count

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render (request,"books/index.html",{
        "books" : books
    })


def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"books/create.html",{
        "form" : form
    })

def edit(request,id):

    
    exists = Book.objects.filter(id=id).exists()
    if exists:
    
        book = Book.objects.get(pk=id)
        form = BookForm(request.POST or None , instance=book)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request,"books/edit.html",{
            "form" : form,
            "book" : book
        })

    return redirect("index")

def delete(request,id):
    exists = Book.objects.filter(id=id).exists()
    if exists:
    
        book = Book.objects.get(pk=id)
        book.delete()
        return redirect("index")
    return redirect("index")