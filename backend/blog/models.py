from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='directory', null=True)
    category = models.ForeignKey('blog.Category', related_name='posts', on_delete=models.CASCADE)
    owner = models.ForeignKey('blog.User', related_name='posts', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
