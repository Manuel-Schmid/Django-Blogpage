import graphene
from django.db.models import Q
from taggit.models import Tag

from ..models import Category, Post, User
from .types import Post as PostType, Category as CategoryType, User as UserType


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID())
    posts = graphene.List(PostType, category_slug=graphene.String(), tag_slug=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.ID())

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_category_by_id(root, info, id):
        return Category.objects.get(pk=id)

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)

    def resolve_posts(root, info, **kwargs):
        category_slug = kwargs.get('category_slug', None)
        tag_slug = kwargs.get('tag_slug', None)

        post_filter = Q()
        if category_slug is not None and tag_slug is not None:
            tag_slug_id = Tag.objects.get(slug=tag_slug)
            post_filter = (
                Q(tagged_items__tag_id=tag_slug_id, category__slug=category_slug)
            )
        elif category_slug is not None:
            post_filter = (
                Q(category__slug=category_slug)
            )
        elif tag_slug is not None:
            tag_slug_id = Tag.objects.get(slug=tag_slug)
            post_filter = (
                Q(tagged_items__tag_id=tag_slug_id)
            )
        return Post.objects \
            .select_related('category', 'owner') \
            .prefetch_related('tags', 'owner__posts', 'owner__posts__tags', 'owner__posts__category') \
            .filter(post_filter)

    def resolve_post_by_slug(root, info, slug):
        return Post.objects.get(slug=slug)
