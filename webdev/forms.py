from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'publisher_name', 'publisher_age', 'page_number', 'publish_date', 'book_type']