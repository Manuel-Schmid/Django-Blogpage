import graphene
from django.core.paginator import Paginator
from django.db.models import Q
from taggit.models import Tag, TaggedItem
from ..models import Category, Post, User
from .types import \
    Post as PostType, \
    PaginationPosts as PaginationPostsType, \
    Category as CategoryType, \
    User as UserType, \
    Tag as TagType


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID())
    users = graphene.List(UserType)
    user = graphene.Field(UserType)
    tags = graphene.List(TagType)
    used_tags = graphene.List(TagType, category_slug=graphene.String(required=False))
    paginated_posts = graphene.Field(PaginationPostsType,
                                     category_slug=graphene.String(),
                                     tag_slugs=graphene.String(),
                                     active_page=graphene.Int())
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
        category_slug = kwargs.get('category_slug', None)

        tag_filter = Q()
        if category_slug is not None:
            category_posts = list(
                Post.objects.select_related('category')
                .prefetch_related('tags')
                .filter(category__slug=category_slug)
                .values_list('id', flat=True)
            )
            tag_filter &= Q(object_id__in=category_posts)

        tags = [obj.tag for obj in TaggedItem.objects.select_related('tag').filter(tag_filter)]
        return list(set(tags))

    def resolve_paginated_posts(root, info, **kwargs):
        category_slug = kwargs.get('category_slug', None)
        tag_slugs = kwargs.get('tag_slugs', None)
        active_page = kwargs.get('active_page', 1)

        post_filter = Q()
        if tag_slugs is not None:
            tag_slugs_list = tag_slugs.split(',')

            # or
            for tag in tag_slugs_list:
                post_filter |= Q(tagged_items__tag__slug__contains=tag)

            # and
            # tag_filter = Q()
            # for tag in tag_slugs_list:
            #     tag_filter |= Q(tag__slug=tag)
            # tagged_posts = list(
            #     TaggedItem.objects
            #     .select_related('tag')
            #     .values('object_id')
            #     .annotate(Count('object_id'))
            #     .filter(tag_filter)
            #     .filter(object_id__count=len(tag_slugs_list))
            #     .values_list('object_id', flat=True))
            # post_filter &= Q(id__in=tagged_posts)

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

        posts = list(set([obj for obj in posts]))

        paginator = Paginator(posts, 4)
        pagination_posts = PaginationPostsType()
        pagination_posts.posts = paginator.page(active_page)
        pagination_posts.num_post_pages = paginator.num_pages
        return pagination_posts

    def resolve_post_by_slug(root, info, slug):
        return Post.objects.get(slug=slug)
