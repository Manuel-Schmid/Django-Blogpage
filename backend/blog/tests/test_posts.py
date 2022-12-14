import json
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_posts(posts):
    assert len(posts) == 2


create_post_query = '''
        mutation CreatePost($input: PostInput!) {
          createPost(postInput: $input) {
            post {
              title
              text
              slug
              owner{
                username
              }
              category {
                name
              }
            }
            success
            errors
          }
        }
        '''

update_post_query = '''
        mutation UpdatePost($input: PostInput!) {
          updatePost(postInput: $input) {
            post {
              title
              slug
              text
              owner{
                username
              }
              category {
                name
              }
            }
            success
            errors
          }
        }
        '''


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post(client_query, categories, users):
    post_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "category": 1,
            "owner": 1,
        }
    }

    response = client_query(create_post_query, variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_post = data.get('createPost', None)
    assert data_create_post is not None
    assert data_create_post['success'] is True
    data_post = data_create_post.get('post', None)
    assert data_post is not None
    assert data_post['title'] == 'test'
    assert data_post['text'] == 'this a test'
    assert data_post['owner']['username'] == 'test_user1'
    assert data_post['category']['name'] == 'test_category1'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_too_long_fields(client_query, categories, users):
    post_input = {
        "input": {
            "title": "e" * 201,
            "text": "this a test",
            "category": 1,
            "owner": 1,
        }
    }

    response = client_query(create_post_query, variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_post = data.get('createPost', None)
    assert data_create_post is not None
    assert data_create_post['success'] is False
    data_post = data_create_post.get('post', None)
    assert data_post is None
    assert 'title' in data_create_post['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_invalid_owner_id(client_query, categories, users):
    post_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "category": 1,
            "owner": 100,
        }
    }

    response = client_query(create_post_query, variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_post = data.get('createPost', None)
    assert data_create_post is not None
    assert data_create_post['success'] is False
    data_post = data_create_post.get('post', None)
    assert data_post is None
    assert 'owner' in data_create_post['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_invalid_category_id(client_query, categories, users):
    post_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "category": 100,
            "owner": 1,
        }
    }

    response = client_query(create_post_query, variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_post = data.get('createPost', None)
    assert data_create_post is not None
    assert data_create_post['success'] is False
    data_post = data_create_post.get('post', None)
    assert data_post is None
    assert 'category' in data_create_post['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_post(client_query, posts):
    post_input = {
        "input": {
            "slug": "test-post1",
            "title": "Test Post3",
            "text": "test_text3",
            "category": 2,
            "owner": 2,
        }
    }

    response = client_query(update_post_query, variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_update_post = data.get('updatePost', None)
    assert data_update_post is not None
    assert data_update_post['success'] is True
    data_post = data_update_post.get('post', None)
    assert data_post is not None
    assert data_post['title'] == 'Test Post3'
    assert data_post['slug'] == 'test-post1'
    assert data_post['text'] == 'test_text3'
    assert data_post['owner']['username'] == 'test_user2'
    assert data_post['category']['name'] == 'test_category2'
