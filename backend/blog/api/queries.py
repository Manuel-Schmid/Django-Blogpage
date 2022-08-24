import graphene
from ..models import Category, Post, User
from .types import Post as PostType, Category as CategoryType, User as UserType


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID())
    posts = graphene.List(PostType, category_slug=graphene.String())
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
        slg = kwargs.get('category_slug', None)
        if slg is not None:
            return Post.objects \
                .select_related('category', 'owner') \
                .prefetch_related('tags', 'owner__posts', 'owner__posts__tags', 'owner__posts__category') \
                .filter(category__slug=slg)
        else:
            return Post.objects \
                .select_related('category', 'owner') \
                .prefetch_related('tags', 'owner__posts', 'owner__posts__tags', 'owner__posts__category') \
                .all()

    def resolve_post_by_slug(root, info, slug):
        return Post.objects.get(slug=slug)
