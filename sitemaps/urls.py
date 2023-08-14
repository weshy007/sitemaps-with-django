from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views
from .sitemaps import ArticleSitemap, AuthorSitemap, StaticPagesSitemap

sitemaps = {
    "articles": ArticleSitemap,
    "authors": AuthorSitemap,
    "static": StaticPagesSitemap,
}

urlpatterns = [
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('author/<slug:slug>/', views.author_detail, name='author_detail'),
    path("about_us", views.about_us, name="about_us"),

    path("sitemap", sitemap, {"sitemaps": sitemaps}, name="sitemap", ),

]