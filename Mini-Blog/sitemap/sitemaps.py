from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from article.models import Post


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()
    
    def location(self, item):
      return reverse('post_detail', args=[item.pk])