import graphene


class PostInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    title = graphene.String()
    slug = graphene.String(required=False)
    text = graphene.String()
    category = graphene.ID()
    owner = graphene.ID()


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    name = graphene.String()


class CommentInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    title = graphene.String()
    text = graphene.String()
    post = graphene.ID()
    owner = graphene.ID()
