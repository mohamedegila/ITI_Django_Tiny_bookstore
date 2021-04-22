from django.db import models
from django.contrib.auth.models import User
from books.utils import create_new_ref_number

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name       = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.name

class Isbn(models.Model):
    author_title = models.CharField(max_length=255,null=True,blank=True)
    book_title   = models.CharField(max_length=255,null=True,blank=True)
    isbn_number  = models.IntegerField(max_length=50,null=True,blank=True,unique=True,default=create_new_ref_number())


    def __str__(self):
        return f"ISBN Number: {self.isbn_number}"

class Book(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    categories  = models.ManyToManyField(Category) 
    author      = models.ForeignKey(User,null=True,on_delete=models.CASCADE, related_name="book")

    isbn        = models.OneToOneField(Isbn,on_delete=models.CASCADE,null=True,blank=True)
    tag         = models.ForeignKey(Tag,null=True,on_delete=models.CASCADE, related_name="book")

    def __str__(self):
        return self.title
 