import json
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_category(categories):
    assert len(categories) == 1


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
    post = content['data']['createPost']['post']

    assert (post is not None)
    assert (post['title'] == 'test')
    assert (post['text'] == 'this a test')
    assert (post['category']['name'] == 'test_category')
    assert (post['owner']['username'] == 'test_user')
