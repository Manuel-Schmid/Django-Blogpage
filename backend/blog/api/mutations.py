import graphene
from graphene_django import DjangoObjectType

from blog.api.inputs import PostInput, CategoryInput
from blog.api.types import Category as CategoryType, Post as PostType
from blog.models import Category, Post


class CreateCategory(graphene.Mutation):
    class Arguments:
        category_input = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, category_input):
        category = Category()
        category.name = category_input.name
        category.save()

        return CreateCategory(category=category)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        category_input = CategoryInput(required=True)
        category_id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, category_input, category_id):
        category = Category.objects.get(pk=category_id)
        category.name = category_input.name
        category.save()

        return UpdateCategory(category=category)


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

class UpdatePost(graphene.Mutation):
    class Arguments:
        post_input = PostInput(required=True)
        post_id = graphene.ID()

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, post_input, post_id):
        post = Post.objects.get(pk=post_id)
        post.title = post_input.title
        post.text = post_input.text
        post.category_id = post_input.category_id
        post.owner_id = post_input.owner_id
        post.save()

        return UpdatePost(post=post)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
