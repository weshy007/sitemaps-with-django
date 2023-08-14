from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Article, Author

class ArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Article.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse('article_detail', args=[obj.slug])
    

class AuthorSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Author.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse('author_detail', args=[obj.slug])


class StaticPagesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['about_us']
    
    def location(self, item):
        return reverse(item)
    
