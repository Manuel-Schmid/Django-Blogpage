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


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category()
        category.name = name
        category.save()

        return CreateCategory(category=category)


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
            # 'category',
            'owner',
            'date_created',
        )


class PostInput(graphene.InputObjectType):
    title = graphene.String()
    text = graphene.String()
    category_id = graphene.Int()
    owner_id = graphene.Int()


class CreatePost(graphene.Mutation):

    class Arguments:
        post_input = PostInput(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, post_input):
        post = Post()
        post.title = post_input.title
        post.text = post_input.text
        post.category_id = post_input.category_id
        post.owner_id = post_input.owner_id
        post.save()
        return CreatePost(post=post)


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


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
