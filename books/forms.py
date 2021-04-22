from django import forms
from .models import Book
from django.core.exceptions import ValidationError 

class BookForm(forms.ModelForm):
    class Meta:
        model   = Book
        fields  = "__all__"
        exclude = ("isbn",)

    def clean(self):
        super(BookForm,self).clean()
        title    = self.cleaned_data.get('title')
        category = self.cleaned_data.get('categories')

        if len(title) < 10 or len(title) > 50:
            raise ValidationError("Title must be in between 10 & 50")
        if len(category) < 2:
            raise ValidationError("Category must be at least 2")
        return self.cleaned_data
