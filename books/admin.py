from django.contrib import admin
from .models import Book
from .models import Category
from .models import Isbn
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Isbn)


