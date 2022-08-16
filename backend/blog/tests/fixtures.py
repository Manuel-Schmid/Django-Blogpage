import pytest
from graphene_django.utils.testing import graphql_query
from blog.models import Category


@pytest.fixture
def categories():
    Category.objects.create(name="testcategory")
    return Category.objects.all()

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client, graphql_url='/graphql/')

    return func