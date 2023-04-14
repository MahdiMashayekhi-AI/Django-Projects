from django.shortcuts import render
from books.models import Book

def index(request):
    books = Book.objects.order_by('-published')[:3]
    return render(request, 'home_page.html', {'books': books})