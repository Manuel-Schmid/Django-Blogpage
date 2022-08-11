import graphene

class PostInput(graphene.InputObjectType):
    title = graphene.String()
    text = graphene.String()
    category_id = graphene.Int()
    owner_id = graphene.Int()
