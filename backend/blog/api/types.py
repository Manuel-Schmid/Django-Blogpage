import graphene
from graphene_django import DjangoObjectType
from taggit.models import Tag as TagModel
from blog.models import Category as CategoryModel, User as UserModel, Post as PostModel


class Category(DjangoObjectType):
    class Meta:
        model = CategoryModel
        fields = (
            'id',
            'name',
        )


class User(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'posts',
            'email',
            'password',
            'username',
            'first_name',
            'last_name',
        )


class Tag(DjangoObjectType):
    class Meta:
        model = TagModel
        fields = (
            'slug',
            'objects',
        )


class Post(DjangoObjectType):
    tags = graphene.List(Tag)

    def resolve_tags(self, info, **kwargs):
        return self.tags.all()

    class Meta:
        model = PostModel
        fields = (
            'id',
            'title',
            'text',
            'image',
            'category',
            'owner',
            'date_created',
        )
