from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_list , name='books_list'),
    path('books/<int:pk>', views.books_detail , name='books_detail'),
]
