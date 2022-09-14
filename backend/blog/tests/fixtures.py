import pytest
from graphene_django.utils.testing import graphql_query
from graphene_file_upload.django.testing import file_graphql_query
from taggit.models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType
from blog.models import Category, User, Post, Comment, PostLike


@pytest.fixture
def users():
    user1 = User.objects.create(username='test_user1')
    user1.set_password('password1')
    user1.save()
    user2 = User.objects.create(username='test_user2')
    user2.set_password('password2')
    user2.save()
    return User.objects.all()


@pytest.fixture
def auth(users, client_query):
    auth_query = '''
        mutation TokenAuth($username: String!, $password: String!) {
          tokenAuth(username: $username, password: $password) {
            token
            payload
            refreshExpiresIn
          }
        }
        '''
    credentials = {
        "username": 'test_user1',
        "password": 'password1'
    }
    return client_query(auth_query, variables=credentials)


@pytest.fixture
def tags(posts):
    content_type = ContentType.objects.get(app_label='blog', model='post')
    tag1 = Tag.objects.create(name='tag_1', slug='tag_1_slug')
    TaggedItem.objects.create(tag=tag1, object_id=posts[0].id, content_type=content_type)
    tag2 = Tag.objects.create(name='tag_2', slug='tag_2_slug')
    TaggedItem.objects.create(tag=tag2, object_id=posts[1].id, content_type=content_type)
    Tag.objects.create(name='tag_3', slug='tag_3_slug')
    return Tag.objects.all()


@pytest.fixture
def categories():
    Category.objects.create(name='test_category1', slug='test_category1')
    Category.objects.create(name='test_category2', slug='test_category2')
    return Category.objects.all()


@pytest.fixture
def comments(posts, users):
    Comment.objects.create(title='test_comment1', post=posts[0], owner=users[0])
    Comment.objects.create(title='test_comment2', post=posts[1], owner=users[1])
    return Comment.objects.all()


@pytest.fixture
def posts(categories, users):
    Post.objects.create(
        title='Test Post1',
        text='test_text1',
        owner=users[0],
        category=categories[0],
    )
    Post.objects.create(
        title='Test Post2',
        text='test_text2',
        owner=users[1],
        category=categories[1],
    )
    return Post.objects.all()


@pytest.fixture
def post_likes(posts, users):
    PostLike.objects.create(
        user=users[0],
        post=posts[1]
    )
    PostLike.objects.create(
        user=users[1],
        post=posts[1]
    )
    return PostLike.objects.all()


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
