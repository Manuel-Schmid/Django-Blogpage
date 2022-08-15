from django.forms import ModelForm
from blog.models import User, Category, Post


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'first_name', 'last_name']  # 'posts'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'owner']

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['text'].required = False