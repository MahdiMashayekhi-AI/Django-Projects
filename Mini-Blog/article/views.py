from django.shortcuts import render
from .models import Post

# Create your views here.

def post_detail(request, slug):
    return render(request, 'article/post_detail.html', {'post': post})