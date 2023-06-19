from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from article.models import Post

# Create your views here.

def test(request):
    return render(request, 'web/test.html')

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'web/home.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get 5 last post:
        recent_posts = Post.objects.order_by('-created_at')[:5]
        context['recent_posts'] = recent_posts
        return context
    

class RegisterPageView(View):
    template_name = 'web/auth/register.html'

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, context)