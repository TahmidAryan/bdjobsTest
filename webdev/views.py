from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.
def saveBookInfo(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewAllBooks')
    else:
        form = BookForm()
    return render(request, 'saveBookInfo.html', {'form': form})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('viewAllBooks')

def viewAllBooks(request):
    books = Book.objects.all()
    return render(request, 'viewAllBooks.html', {'books': books})

