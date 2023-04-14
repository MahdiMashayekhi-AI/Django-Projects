from django.shortcuts import render
from .models import Book

# Create your views here.

def books_list(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books_list.html', context)


def books_detail(request, pk):
    book = Book.objects.get(id=pk)

    context = {
        'book': book,
    }

    return render(request, 'books_detail.html', context)