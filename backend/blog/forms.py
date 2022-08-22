from django.forms import ModelForm
from blog.models import User, Category, Post, Comment


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'first_name', 'last_name']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'category', 'owner']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'text', 'post', 'owner']
