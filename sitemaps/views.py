from django.shortcuts import HttpResponse, get_object_or_404, render

from .models import Article, Author


# Create your views here.
def article_detail(request, slug):
    post = get_object_or_404(Article, slug=slug)
    return render(request, 'article_detail.html', {'post': post})


def author_detail(request, slug):
    post = get_object_or_404(Author, slug=slug)
    return render(request, 'author_detail.html', {'post': post})

def about_us(request):
    return HttpResponse("About Us Page!")