import graphene


class PostInput(graphene.InputObjectType):
    slug = graphene.String(required=False)
    title = graphene.String()
    text = graphene.String()
    category = graphene.ID()
    owner = graphene.ID()


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    slug = graphene.String(required=False)
    name = graphene.String()


class CommentInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    title = graphene.String()
    text = graphene.String()
    post = graphene.ID()
    owner = graphene.ID(required=False)


class PostLikeInput(graphene.InputObjectType):
    post = graphene.ID()
    user = graphene.ID()
