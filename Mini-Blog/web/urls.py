from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='web/auth/login.html'), name='login'),
    path('register/', views.RegisterPageView.as_view(template_name='web/auth/register.html'), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('test/', views.test, name='test'),
]