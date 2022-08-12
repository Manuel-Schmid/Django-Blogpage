from django.forms import ModelForm
from blog.models import User, Category, Post


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['posts', 'email', 'password', 'username', 'first_name', 'last_name']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'owner', 'date_created']
