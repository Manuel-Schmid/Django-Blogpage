import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation

from blog.api.inputs import PostInput, CategoryInput
from blog.api.types import Category as CategoryType, Post as PostType
from blog.models import Category, Post
from blog.forms import CategoryForm, PostForm


class CategoryMutation(DjangoModelFormMutation):
    category = graphene.Field(CategoryType)

    class Meta:
        form_class = CategoryForm
        lookup_field = 'id'


class PostMutation(DjangoModelFormMutation):
    post = graphene.Field(PostType)

    class Meta:
        form_class = PostForm
        lookup_field = 'id'


# class CreatePost(graphene.Mutation):
#
#     class Arguments:
#         post_input = PostInput(required=True)
#
#     post = graphene.Field(PostType)
#
#     @classmethod
#     def mutate(cls, root, info, post_input):
#         post = Post()
#         post.title = post_input.title
#         post.text = post_input.text
#         post.category_id = post_input.category_id
#         post.owner_id = post_input.owner_id
#         post.save()
#         return CreatePost(post=post)
#
#
# class UpdatePost(graphene.Mutation):
#     class Arguments:
#         post_input = PostInput(required=True)
#         post_id = graphene.ID()
#
#     post = graphene.Field(PostType)
#
#     @classmethod
#     def mutate(cls, root, info, post_input, post_id):
#         post = Post.objects.get(pk=post_id)
#         post.title = post_input.title
#         post.text = post_input.text
#         post.category_id = post_input.category_id
#         post.owner_id = post_input.owner_id
#         post.save()
#
#         return UpdatePost(post=post)


class Mutation(graphene.ObjectType):
    create_category = CategoryMutation.Field()
    update_category = CategoryMutation.Field()
    create_post = PostMutation.Field()
    update_post = PostMutation.Field()
