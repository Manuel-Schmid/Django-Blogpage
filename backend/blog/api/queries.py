import graphene
from django.db.models import Q
from taggit.models import Tag, TaggedItem
from ..models import Category, Post, User, Comment, PostLike
from .types import Post as PostType, Category as CategoryType, User as UserType, Tag as TagType, PostLike as PostLikeType, CommentLike as CommentLikeType


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID())
    users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.ID())
    tags = graphene.List(TagType)
    used_tags = graphene.List(TagType)
    posts = graphene.List(PostType, category_slug=graphene.String(), tag_slug=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    post_like = graphene.Field(PostLikeType, post_id=graphene.ID(), user_id=graphene.ID())


    def resolve_post_like(root, info, **kwargs):
        post_id = kwargs.get('post_id', None)
        user_id = kwargs.get('user_id', None)
        if post_id is None or user_id is None:
            return None
        return PostLike.objects.filter(post=post_id, user=user_id).first()

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_category_by_id(root, info, id):
        return Category.objects.get(pk=id)

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_user_by_id(root, info, id):
        return User.objects.get(pk=id)

    def resolve_tags(root, info, **kwargs):
        return Tag.objects.all()

    def resolve_used_tags(root, info, **kwargs):
        tags = [obj.tag for obj in TaggedItem.objects.select_related('tag').all()]
        return list(set(tags))

    def resolve_posts(root, info, **kwargs):
        category_slug = kwargs.get('category_slug', None)
        tag_slug = kwargs.get('tag_slug', None)

        post_filter = Q()
        if tag_slug is not None:
            post_filter &= Q(tagged_items__tag__slug=tag_slug)

        if category_slug is not None:
            post_filter &= Q(category__slug=category_slug)

        return Post.objects \
            .select_related('category', 'owner') \
            .prefetch_related('tags', 'comments', 'comments__owner', 'post_likes', 'owner__posts', 'owner__posts__tags', 'owner__posts__category') \
            .filter(post_filter)

    def resolve_post_by_slug(root, info, slug):
        return Post.objects.get(slug=slug)
