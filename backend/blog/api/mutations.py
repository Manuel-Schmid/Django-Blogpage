import graphene
import graphql_jwt
from graphql_auth import mutations
from graphene_file_upload.scalars import Upload
from blog.api.inputs import PostInput, CategoryInput, CommentInput, PostLikeInput
from blog.api.types import \
    Category as CategoryType, \
    Post as PostType, \
    Comment as CommentType, \
    PostLike as PostLikeType, \
    GraphqlOutput
from blog.models import Post, Category, Comment, PostLike
from blog.forms import CategoryForm, PostForm, PostLikeForm, CreateCommentForm, UpdateCommentForm


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
        user = info.context.user
        if user.is_authenticated:
            post_like_input['user'] = user.id
            form = PostLikeForm(data=post_like_input)
            if form.is_valid():
                post_like = form.save()
                return CreatePostLike(post_like=post_like, success=True)
            return CreatePostLike(success=False, errors=form.errors.get_json_data())
        return CreatePostLike(success=False)


class DeletePostLike(graphene.Mutation, GraphqlOutput):
    success = graphene.Boolean()

    class Arguments:
        post_like_input = PostLikeInput(required=True)

    @classmethod
    def mutate(cls, root, info, post_like_input):
        user = info.context.user
        if user.is_authenticated:
            PostLike.objects.filter(post=post_like_input.post, user=user.id).delete()
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
        user = info.context.user
        if user.is_authenticated:
            comment_input['owner'] = user.id
            form = CreateCommentForm(data=comment_input)
            if form.is_valid():
                comment = form.save()
                return CreateComment(comment=comment, success=True)
            return CreateComment(success=False, errors=form.errors.get_json_data())
        return CreateComment(success=False)


class UpdateComment(graphene.Mutation, GraphqlOutput):
    comment = graphene.Field(CommentType)

    class Arguments:
        comment_input = CommentInput(required=True)

    @classmethod
    def mutate(cls, root, info, comment_input):
        comment = Comment.objects.get(pk=comment_input.get('id'))
        form = UpdateCommentForm(instance=comment, data=comment_input)
        if form.is_valid():
            comment = form.save()
            return UpdateComment(comment=comment, success=True)
        return UpdateComment(success=False, errors=form.errors.get_json_data())


class DeleteComment(graphene.Mutation, GraphqlOutput):
    success = graphene.Boolean()

    class Arguments:
        comment_id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, comment_id):
        user = info.context.user
        if user.is_authenticated:
            Comment.objects.filter(pk=comment_id, owner_id=user.id).delete()
        return cls(success=True)


class UploadMutation(graphene.Mutation, GraphqlOutput):
    class Arguments:
        file_input = Upload(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, file_input):
        print(file_input)

        return UploadMutation(success=True)


class AuthMutation(graphene.ObjectType):
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_post_like = CreatePostLike.Field()
    delete_post_like = DeletePostLike.Field()
    create_comment = CreateComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
    test_mutation = UploadMutation.Field()
