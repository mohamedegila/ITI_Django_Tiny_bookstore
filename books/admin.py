from django.contrib import admin
from .models import Book, Category, Isbn, Tag

from .forms import BookForm, CategoryForm
from django.contrib.auth.models import User

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display  = ('title','author')
    ordering = ('title',)
    list_filter   = ('categories',)
    search_fields = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

class BookInline(admin.StackedInline):
    model    = Book
    max_num  = 3
    extra    = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [BookInline]

class IsbnAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    
admin.site.register(Book,BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Isbn,IsbnAdmin)
admin.site.register(Tag,TagAdmin)


