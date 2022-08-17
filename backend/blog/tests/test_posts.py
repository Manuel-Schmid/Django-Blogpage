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
            "owner": 1
        }
    }

    response = client_query(create_post_query,variables=post_input)

    content = json.loads(response.content)
    assert (content is not None)
    assert (content['data'] is not None)
    data_create_post = content['data']['createPost']
    assert (data_create_post is not None)
    assert (data_create_post['post'] is not None)
    assert (data_create_post['success'] == True)

    post = data_create_post['post']
    assert (post is not None)
    assert (post['title'] == 'test')
    assert (post['text'] == 'this a test')
    assert (post['owner']['username'] == 'test_user1')
    assert (post['category']['name'] == 'test_category1')


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_too_long_fields(client_query, categories, users):
    post_input = {
        "input": {
            "title": "e" * 201,
            "text": "this a test",
            "category": 1,
            "owner": 1
        }
    }

    response = client_query(create_post_query,variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    assert content['data'] is not None
    data_create_post = content['data']['createPost']
    assert data_create_post is not None
    assert data_create_post['post'] is None
    assert data_create_post['success'] == False
    assert 'title' in data_create_post['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_invalid_owner_id(client_query, categories, users):
    post_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "category": 1,
            "owner": 100
        }
    }

    response = client_query(create_post_query,variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    assert content['data'] is not None
    data_create_post = content['data']['createPost']
    assert data_create_post is not None
    assert data_create_post['post'] is None
    assert data_create_post['success'] == False
    assert 'owner' in data_create_post['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_invalid_category_id(client_query, categories, users):
    post_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "category": 100,
            "owner": 1
        }
    }

    response = client_query(create_post_query,variables=post_input)

    content = json.loads(response.content)
    assert content is not None
    assert content['data'] is not None
    data_create_post = content['data']['createPost']
    assert data_create_post is not None
    assert data_create_post['post'] is None
    assert data_create_post['success'] == False
    assert 'category' in data_create_post['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_post(client_query, posts):
    post_input = {
        "input": {
            "id": 1,
            "title": "test_post3",
            "text": "test_text3",
            "category": 2,
            "owner": 2
        }
    }

    response = client_query(update_post_query,variables=post_input)

    content = json.loads(response.content)
    assert (content is not None)
    assert (content['data'] is not None)
    data_update_post = content['data']['updatePost']
    assert (data_update_post is not None)
    assert (data_update_post['post'] is not None)
    assert (data_update_post['success'] == True)

    post = data_update_post['post']
    assert (post['title'] == 'test_post3')
    assert (post['text'] == 'test_text3')
    assert (post['owner']['username'] == 'test_user2')
    assert (post['category']['name'] == 'test_category2')