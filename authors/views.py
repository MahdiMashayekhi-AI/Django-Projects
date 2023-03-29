from django.shortcuts import render
from .models import Author

# Create your views here.

def authors_list(request):
    authors = Author.objects.all()

    context = {
        'authors': authors,
    }

    return render(request, 'authors_list.html', context)