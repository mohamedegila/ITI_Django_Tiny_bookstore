from django import forms
from .models import Book, Category
from django.core.exceptions import ValidationError 

class BookForm(forms.ModelForm):
    class Meta:
        model   = Book
        fields  = "__all__"
        # exclude = ("isbn",)

    def clean(self):
        super(BookForm,self).clean()
        title    = self.cleaned_data.get('title')
    
        if len(title) < 10 or len(title) > 50:
            raise ValidationError("Title must be in between 10 & 50")
       
        return self.cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = "__all__"

    def clean(self):
        super(CategoryForm,self).clean()

        category_name = self.cleaned_data.get('name')

        if len(category_name) < 2:
            raise ValidationError("Category name must be at least 2")
        return self.cleaned_data