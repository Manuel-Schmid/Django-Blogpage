import graphene

from .api.mutations import Mutation
from .api.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation)
