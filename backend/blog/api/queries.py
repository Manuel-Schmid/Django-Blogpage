import graphene
from ..models import Category, Post, User
from .types import Post as PostType, Category as CategoryType, User as UserType

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    posts = graphene.List(PostType)
    users = graphene.List(UserType)

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_posts(root, info, **kwargs):
        return Post.objects \
            .select_related('category', 'owner') \
            .prefetch_related('tags', 'owner__posts', 'owner__posts__tags', 'owner__posts__category') \
            .all()
