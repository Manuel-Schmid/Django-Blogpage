import graphene

from graphene_file_upload.scalars import Upload
from blog.api.inputs import PostInput, CategoryInput, CommentInput, PostLikeInput
from blog.api.types import Category as CategoryType, Post as PostType, Comment as CommentType, CommentLike as CommentLikeType, PostLike as PostLikeType, GraphqlOutput
from blog.models import Post, Category, Comment, PostLike
from blog.forms import CategoryForm, PostForm, CommentForm, PostLikeForm


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


class CreatePostLike(graphene.Mutation, GraphqlOutput):
    post_like = graphene.Field(PostLikeType)

    class Arguments:
        post_like_input = PostLikeInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_like_input):
        form = PostLikeForm(data=post_like_input)
        if form.is_valid():
            post_like = form.save()
            return CreatePostLike(post_like=post_like, success=True)
        return CreatePostLike(success=False, errors=form.errors.get_json_data())


class DeletePostLike(graphene.Mutation, GraphqlOutput):
    success = graphene.Boolean()

    class Arguments:
        post_like_input = PostLikeInput()

    @classmethod
    def mutate(cls, root, info, post_like_input):
        PostLike.objects.filter(post=post_like_input.post, user=post_like_input.user).delete()
        return cls(success=True)


class UpdatePost(graphene.Mutation, GraphqlOutput):
    post = graphene.Field(PostType)

    class Arguments:
        post_input = PostInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_input):
        post = Post.objects.get(slug=post_input.get('slug'))
        form = PostForm(instance=post, data=post_input)
        if form.is_valid():
            post = form.save()
            return UpdatePost(post=post, success=True)
        return UpdatePost(success=False, errors=form.errors.get_json_data())


class CreateComment(graphene.Mutation, GraphqlOutput):
    comment = graphene.Field(CommentType)

    class Arguments:
        comment_input = CommentInput(required=True)

    @classmethod
    def mutate(cls, root, info, comment_input):
        form = CommentForm(data=comment_input)
        if form.is_valid():
            comment = form.save()
            return CreateComment(comment=comment, success=True)
        return CreateComment(success=False, errors=form.errors.get_json_data())


class UpdateComment(graphene.Mutation, GraphqlOutput):
    comment = graphene.Field(CommentType)

    class Arguments:
        comment_input = CommentInput(required=True)

    @classmethod
    def mutate(cls, root, info, comment_input):
        comment = Comment.objects.get(pk=comment_input.get('id'))
        form = CommentForm(instance=comment, data=comment_input)
        if form.is_valid():
            comment = form.save()
            return UpdateComment(comment=comment, success=True)
        return UpdateComment(success=False, errors=form.errors.get_json_data())


class UploadMutation(graphene.Mutation, GraphqlOutput):
    class Arguments:
        file_input = Upload(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, file_input):
        print(file_input)

        return UploadMutation(success=True)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_post_like = CreatePostLike.Field()
    delete_post_like = DeletePostLike.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    test_mutation = UploadMutation.Field()
