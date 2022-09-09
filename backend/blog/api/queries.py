import graphene
from django.core.paginator import Paginator
from django.db.models import Q
from taggit.models import Tag, TaggedItem
from ..models import Category, Post, User
from .types import \
    Post as PostType,\
    Category as CategoryType, \
    User as UserType, \
    Tag as TagType


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID())
    users = graphene.List(UserType)
    user = graphene.Field(UserType)
    tags = graphene.List(TagType)
    used_tags = graphene.List(TagType)
    posts = graphene.List(PostType, category_slug=graphene.String(), tag_slug=graphene.String(), page_nr=graphene.Int())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_category_by_id(root, info, id):
        return Category.objects.get(pk=id)

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_user(root, info):
        user = info.context.user
        if user.is_authenticated:
            return User.objects.get(pk=info.context.user.id)
        return None

    def resolve_tags(root, info, **kwargs):
        return Tag.objects.all()

    def resolve_used_tags(root, info, **kwargs):
        tags = [obj.tag for obj in TaggedItem.objects.select_related('tag').all()]
        return list(set(tags))

    def resolve_posts(root, info, **kwargs):
        category_slug = kwargs.get('category_slug', None)
        tag_slug = kwargs.get('tag_slug', None)
        page_nr = kwargs.get('page_nr', None)

        post_filter = Q()
        if tag_slug is not None:
            post_filter &= Q(tagged_items__tag__slug=tag_slug)

        if category_slug is not None:
            post_filter &= Q(category__slug=category_slug)

        posts = Post.objects \
            .select_related('category', 'owner') \
            .prefetch_related('tags',
                              'comments',
                              'comments__owner',
                              'post_likes',
                              'post_likes__user',
                              'owner__posts',
                              'owner__posts__tags',
                              'owner__posts__category') \
            .filter(post_filter)

        if page_nr is not None:
            return Paginator(posts, 4).page(page_nr)

        return posts

    def resolve_post_by_slug(root, info, slug):
        return Post.objects.get(slug=slug)
