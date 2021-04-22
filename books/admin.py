from django.contrib import admin
from .models import Book
from .models import Category
from .models import Isbn
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Isbn)


