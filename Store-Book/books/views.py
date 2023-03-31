from django.shortcuts import render
from .models import Book

# Create your views here.

def books_list(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books_list.html', context)