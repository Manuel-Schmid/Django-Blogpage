import json
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_posts(posts):
    assert len(posts) == 2


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

    response = client_query(
        '''
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
          }
        }
        ''',
        variables=post_input
    )

    content = json.loads(response.content)
    assert (content is not None)
    assert (content['data'] is not None)
    assert (content['data']['createPost'] is not None)
    assert (content['data']['createPost']['post'] is not None)

    post = content['data']['createPost']['post']
    assert (post is not None)
    assert (post['title'] == 'test')
    assert (post['text'] == 'this a test')
    assert (post['owner']['username'] == 'test_user1')
    assert (post['category']['name'] == 'test_category1')


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

    response = client_query(
        '''
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
          }
        }
        ''',
        variables=post_input
    )

    content = json.loads(response.content)
    assert (content is not None)
    assert (content['data'] is not None)
    assert (content['data']['updatePost'] is not None)
    assert (content['data']['updatePost']['post'] is not None)

    post = content['data']['updatePost']['post']
    assert (post['title'] == 'test_post3')
    assert (post['text'] == 'test_text3')
    assert (post['owner']['username'] == 'test_user2')
    assert (post['category']['name'] == 'test_category2')