from django.urls import path

from . import views

urlpatterns = [
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('author/<slug:slug>/', views.author_detail, name='author_detail'),
    path("about_us", views.about_us, name="about_us"),
]