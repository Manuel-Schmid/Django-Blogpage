import graphene
from ..models import Category, Post
from .types import Post as PostType, Category as CategoryType

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    posts = graphene.List(PostType)

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_posts(root, info, **kwargs):
        return Post.objects \
            .select_related('category', 'owner') \
            .prefetch_related('tags', 'owner__posts', 'owner__posts__tags', 'owner__posts__category') \
            .all()
