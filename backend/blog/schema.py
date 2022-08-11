import graphene
from graphene_django import DjangoObjectType
from .models import Category, Post, User
from taggit.models import Tag


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'posts',
        )


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = (
            'slug',
            'objects'
        )


class PostType(DjangoObjectType):
    tags = graphene.List(TagType)

    def resolve_tags(self, info, **kwargs):
        return self.tags.all()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'image',
            'category',
            'owner',
            'date_created',
        )


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    posts = graphene.List(PostType)

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_posts(root, info, **kwargs):
        return Post.objects\
            .select_related('category', 'owner')\
            .prefetch_related('tags', 'owner__posts', 'owner__posts__tags', 'owner__posts__category')\
            .all()


schema = graphene.Schema(query=Query)
