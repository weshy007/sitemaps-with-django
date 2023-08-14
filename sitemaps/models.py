import uuid

from django.db import models
from django.urls import reverse


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(Base):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    slug = models.SlugField(unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author_detail', args=[self.slug])
    

class Article(Base):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('author_detail', args=[self.slug])