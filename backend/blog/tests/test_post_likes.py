import json
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_likes(auth, post_likes):
    assert len(post_likes) == 2


create_post_like_query = '''
        mutation createPostLike($postLikeInput: PostLikeInput!) {
          createPostLike(postLikeInput: $postLikeInput) {
            postLike {
              id
            }
          }
        }
        '''

delete_post_like_query = '''
        mutation deletePostLike($postLikeInput: PostLikeInput!) {
          deletePostLike(postLikeInput: $postLikeInput) {
            success
          }
        }
        '''


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post_like(auth, client_query, post_likes):
    post_like_input = {
        "postLikeInput": {
            "post": 1,
        }
    }

    response = client_query(create_post_like_query, variables=post_like_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_post_likes = data.get('createPostLike', None)
    assert data_post_likes is not None

    post_like = data_post_likes.get('postLike', None)
    assert post_like is not None
    post = post_like.get('id', None)
    assert post is not None


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_delete_post_like(auth, client_query, post_likes):
    post_like_input = {
        "postLikeInput": {
            "post": 2,
        }
    }

    response = client_query(delete_post_like_query, variables=post_like_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_post_likes = data.get('deletePostLike', None)
    assert data_post_likes is not None

    success = data_post_likes.get('success', None)
    assert success is not None
    assert success
