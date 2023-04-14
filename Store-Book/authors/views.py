from django.shortcuts import render, get_object_or_404
from .models import Author

# Create your views here.

def authors_list(request):
    authors = Author.objects.all()

    context = {
        'authors': authors,
    }

    return render(request, 'authors_list.html', context)


def authors_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    context = {
        'author': author,
    }
    return render(request, 'authors_detail.html', context)