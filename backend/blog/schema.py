import graphene

from .api.mutations import CreateCategory, CreatePost
from .models import Category, Post
from .api.types import Post as PostType

class Query(graphene.ObjectType):
    categories = graphene.List(Category)
    posts = graphene.List(PostType)

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_posts(root, info, **kwargs):
        return Post.objects \
            .select_related('category', 'owner') \
            .prefetch_related('tags', 'owner__posts', 'owner__posts__tags', 'owner__posts__category') \
            .all()

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
