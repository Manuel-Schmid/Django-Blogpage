import json
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_comments(comments):
    assert len(comments) == 2


create_comment_query = '''
        mutation CreateComment($input: CommentInput!) {
          createComment(commentInput: $input) {
            comment {
              title
              text
              post {
                title
              }
                owner{
                username
              }
            }
            success
            errors
            }
        }
        '''

update_comment_query = '''
        mutation UpdateComment($input: CommentInput!) {
          updateComment(commentInput: $input) {
            comment {
              title
              text
              post {
                title
              }
                owner{
                username
              }
            }
            success
            errors
            }
        }
        '''


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_comment(client_query, posts):
    comment_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "post": 1,
            "owner": 1,
        }
    }

    response = client_query(create_comment_query, variables=comment_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_comment = data.get('createComment', None)
    assert data_create_comment is not None
    assert data_create_comment['success'] is True
    data_comment = data_create_comment.get('comment', None)
    assert data_comment is not None
    assert data_comment['title'] == 'test'
    assert data_comment['text'] == 'this a test'
    assert data_comment['post']['title'] == 'test_post1'
    assert data_comment['owner']['username'] == 'test_user1'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_comment_too_long_fields(client_query, posts):
    comment_input = {
        "input": {
            "title": "e" * 201,
            "text": "this a test",
            "post": 1,
            "owner": 1,
        }
    }

    response = client_query(create_comment_query, variables=comment_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_comment = data.get('createComment', None)
    assert data_create_comment is not None
    assert data_create_comment['success'] is False
    data_comment = data_create_comment.get('comment', None)
    assert data_comment is None
    assert 'title' in data_create_comment['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_comment_invalid_post_id(client_query, users):
    comment_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "post": 1,
            "owner": 1,
        }
    }

    response = client_query(create_comment_query, variables=comment_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_comment = data.get('createComment', None)
    assert data_create_comment is not None
    assert data_create_comment['success'] is False
    data_comment = data_create_comment.get('comment', None)
    assert data_comment is None
    assert 'post' in data_create_comment['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_comment_invalid_owner_id(client_query, posts):
    comment_input = {
        "input": {
            "title": "test",
            "text": "this a test",
            "post": 1,
            "owner": 100,
        }
    }

    response = client_query(create_comment_query, variables=comment_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_comment = data.get('createComment', None)
    assert data_create_comment is not None
    assert data_create_comment['success'] is False
    data_comment = data_create_comment.get('comment', None)
    assert data_comment is None
    assert 'owner' in data_create_comment['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_comment(client_query, comments):
    comment_input = {
        "input": {
            "id": 1,
            "title": "test_comment3",
            "text": "test_text3",
            "post": 2,
            "owner": 2,
        }
    }

    response = client_query(update_comment_query, variables=comment_input)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_create_comment = data.get('updateComment', None)
    assert data_create_comment is not None
    assert data_create_comment['success'] is True
    data_comment = data_create_comment.get('comment', None)
    assert data_comment is not None
    assert data_comment['title'] == 'test_comment3'
    assert data_comment['text'] == 'test_text3'
    assert data_comment['post']['title'] == 'test_post2'
    assert data_comment['owner']['username'] == 'test_user2'
