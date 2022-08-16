import pytest
from graphene_django.utils.testing import graphql_query
from blog.models import Category, User, Post


@pytest.fixture
def users():
    User.objects.create(username="test_user1")
    User.objects.create(username="test_user2")
    return User.objects.all()


@pytest.fixture
def categories():
    Category.objects.create(name="test_category1")
    Category.objects.create(name="test_category2")
    return Category.objects.all()


@pytest.fixture
def posts(categories, users):
    Post.objects.create(
        title="test_post1",
        text="test_text1",
        owner=users[0],
        category=categories[0],
    )
    Post.objects.create(
        title="test_post2",
        text="test_text2",
        owner=users[1],
        category=categories[1],
    )
    return Post.objects.all()


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client, graphql_url='/graphql/')

    return func
