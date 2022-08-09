from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

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
    tags = TaggableManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey('blog.User', related_name='comments', on_delete=models.CASCADE)

class CommentLike(models.Model):
    comment = models.ForeignKey('blog.Comment', related_name='comment_likes', on_delete=models.CASCADE)
    user = models.ForeignKey('blog.User', related_name='comment_likes', on_delete=models.CASCADE)

class PostLike(models.Model):
    post = models.ForeignKey('blog.Post', related_name='post_likes', on_delete=models.CASCADE)
    user = models.ForeignKey('blog.User', related_name='post_likes', on_delete=models.CASCADE)
