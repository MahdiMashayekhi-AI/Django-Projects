from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.authors_list , name='authors_list'),
    path('authors/<int:pk>', views.authors_detail , name='authors_detail'),
]
