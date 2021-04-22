from django.contrib import admin
from .models import Book
from .models import Category
from .models import Isbn
from .forms import BookForm
# Register your models here.

class BookAdmin(admin.ModelAdmin):

    form = BookForm
    list_display  = ('title','author')
    list_filter   = ('categories',)
    search_fields = ('title',)

admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn)


