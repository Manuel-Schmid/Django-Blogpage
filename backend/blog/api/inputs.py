import graphene


class PostInput(graphene.InputObjectType):
    title = graphene.String()
    text = graphene.String()
    category_id = graphene.ID()
    owner_id = graphene.ID()


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()
