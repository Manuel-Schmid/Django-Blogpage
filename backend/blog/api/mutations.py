import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from blog.api.inputs import PostInput
from blog.api.types import Category as CategoryType, Post as PostType
from blog.models import Post
from blog.forms import CategoryForm, PostForm


class CategoryMutation(DjangoModelFormMutation):
    category = graphene.Field(CategoryType)

    class Meta:
        form_class = CategoryForm
        lookup_field = 'id'


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
    create_category = CategoryMutation.Field()
    update_category = CategoryMutation.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
