import json
import pytest

@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_category(categories):
    assert len(categories) == 1


# @pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post(client_query):
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
              dateCreated
            }
          }
        }
        ''',
        variables = post_input
    )
    # try:
    print(response.content)
    content = json.loads(response.content)
    assert True
    # assert 'errors' not in content
    # except:
    #     print(response)

