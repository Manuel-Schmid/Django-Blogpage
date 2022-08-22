import pytest
from graphene_django.utils.testing import graphql_query
from graphene_file_upload.django.testing import file_graphql_query
from blog.models import Category, User, Post, Comment


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
def comments(posts, users):
    Comment.objects.create(title="test_comment1", post=posts[0], owner=users[0])
    Comment.objects.create(title="test_comment2", post=posts[1], owner=users[1])
    return Comment.objects.all()


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


@pytest.fixture
def client_query_file(client):
    def func(*args, **kwargs):
        return file_graphql_query(*args, **kwargs, client=client, graphql_url='/graphql/')

    return func
