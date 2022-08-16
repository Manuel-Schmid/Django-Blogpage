import graphene
# from graphene_django.forms.mutation import DjangoModelFormMutation

from blog.api.inputs import PostInput, CategoryInput
from blog.api.types import Category as CategoryType, Post as PostType
from blog.models import Post, Category
from blog.forms import CategoryForm, PostForm


class UpdateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        category_input = CategoryInput(required=True)

    @classmethod
    def mutate(cls, root, info, category_input):
        category = Category.objects.get(pk=category_input.get('id'))
        form = CategoryForm(instance=category, data=category_input)
        if form.is_valid():
            category = form.save()
            return CreateCategory(category=category)
        print(form.errors.get_json_data())
        return CreateCategory()


class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        category_input = CategoryInput(required=True)

    @classmethod
    def mutate(cls, root, info, category_input):
        form = CategoryForm(data=category_input)
        if form.is_valid():
            category = form.save()
            return CreateCategory(category=category)
        print(form.errors.get_json_data())
        return CreateCategory()


class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        post_input = PostInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_input):
        form = PostForm(data=post_input)
        if form.is_valid():
            post = form.save()
            return CreatePost(post=post)
        print(form.errors.get_json_data())
        return CreatePost()


class UpdatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        post_input = PostInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_input):
        post = Post.objects.get(pk=post_input.get('id'))
        form = PostForm(instance=post, data=post_input)
        if form.is_valid():
            post = form.save()
            return CreatePost(post=post)
        print(form.errors.get_json_data())
        return CreatePost()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
