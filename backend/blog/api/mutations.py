import graphene

from blog.api.inputs import PostInput, CategoryInput
from blog.api.types import Category as CategoryType, Post as PostType, GraphqlOutput
from blog.models import Post, Category
from blog.forms import CategoryForm, PostForm


class UpdateCategory(graphene.Mutation, GraphqlOutput):
    category = graphene.Field(CategoryType)

    class Arguments:
        category_input = CategoryInput(required=True)

    @classmethod
    def mutate(cls, root, info, category_input):
        category = Category.objects.get(pk=category_input.get('id'))
        form = CategoryForm(instance=category, data=category_input)
        if form.is_valid():
            category = form.save()
            return UpdateCategory(category=category, success=True)
        return UpdateCategory(success=False, errors=form.errors.get_json_data())


class CreateCategory(graphene.Mutation, GraphqlOutput):
    category = graphene.Field(CategoryType)

    class Arguments:
        category_input = CategoryInput(required=True)

    @classmethod
    def mutate(cls, root, info, category_input):
        form = CategoryForm(data=category_input)
        if form.is_valid():
            category = form.save()
            return CreateCategory(category=category, success=True)
        return CreateCategory(success=False, errors=form.errors.get_json_data())


class CreatePost(graphene.Mutation, GraphqlOutput):
    post = graphene.Field(PostType)

    class Arguments:
        post_input = PostInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_input):
        form = PostForm(data=post_input)
        if form.is_valid():
            post = form.save()
            return CreatePost(post=post, success=True)
        return CreatePost(success=False, errors=form.errors.get_json_data())


class UpdatePost(graphene.Mutation, GraphqlOutput):
    post = graphene.Field(PostType)

    class Arguments:
        post_input = PostInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_input):
        post = Post.objects.get(pk=post_input.get('id'))
        form = PostForm(instance=post, data=post_input)
        if form.is_valid():
            post = form.save()
            return UpdatePost(post=post, success=True)
        return UpdatePost(success=False, errors=form.errors.get_json_data())


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
