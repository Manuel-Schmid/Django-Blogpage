import graphene
from graphene_django import DjangoObjectType
from graphene_django.utils import camelize
from taggit.models import Tag as TagModel
from blog.models import Category as CategoryModel, User as UserModel, Post as PostModel, Comment as CommentModel


class GraphqlError(graphene.Scalar):
    class Meta:
        description = """
            Errors messages and codes mapped to
            fields or non fields errors.
            Example:
            {
                field_name: [
                    {
                        "message": "error message",
                        "code": "error_code"
                    }
                ],
                other_field: [
                    {
                        "message": "error message",
                        "code": "error_code"
                    }
                ],
                nonFieldErrors: [
                    {
                        "message": "error message",
                        "code": "error_code"
                    }
                ]
            }
        """

    @staticmethod
    def serialize(errors):
        if isinstance(errors, dict):
            if errors.get("__all__", False):
                errors["non_field_errors"] = errors.pop("__all__")
            return camelize(errors)
        if isinstance(errors, list):
            return {"nonFieldErrors": errors}
        raise Exception("`errors` must be list or dict!")


class GraphqlOutput:
    success = graphene.Boolean(default_value=True)
    errors = graphene.Field(GraphqlError)


class Category(DjangoObjectType):
    class Meta:
        model = CategoryModel
        fields = (
            'id',
            'name',
        )


class User(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'posts',
            'email',
            'password',
            'username',
            'first_name',
            'last_name',
        )


class Tag(DjangoObjectType):
    class Meta:
        model = TagModel
        fields = (
            'slug',
            'name',
        )


class Post(DjangoObjectType):
    tags = graphene.List(Tag)

    def resolve_tags(self, info, **kwargs):
        return self.tags.all()

    class Meta:
        model = PostModel
        fields = (
            'id',
            'title',
            'slug',
            'text',
            'image',
            'category',
            'owner',
            'date_created',
        )


class Comment(DjangoObjectType):

    class Meta:
        model = CommentModel
        fields = (
            'id',
            'title',
            'text',
            'post',
            'owner',
        )
