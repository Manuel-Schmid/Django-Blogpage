import json
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_categories(categories):
    assert len(categories) == 2


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_category(client_query):
    category_input = {
        "input": {
            "name": "test_category4"
        }
    }

    response = client_query(
        '''
        mutation CreateCategory($input: CategoryInput!) {
          createCategory(categoryInput: $input) {
            category {
              name
            }
          }
        }
        ''',
        variables=category_input
    )

    content = json.loads(response.content)
    assert (content is not None)
    assert (content['data'] is not None)
    assert (content['data']['createCategory'] is not None)
    assert (content['data']['createCategory']['category'] is not None)

    category = content['data']['createCategory']['category']
    assert (category is not None)
    assert (category['name'] == 'test_category4')


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_category(client_query, categories):
    category_input = {
        "input": {
            "id": 1,
            "name": "test_category3"
        }
    }

    response = client_query(
        '''
        mutation UpdateCategory($input: CategoryInput!) {
          updateCategory(categoryInput: $input) {
            category {
              id
              name
            }
          }
        }
        ''',
        variables=category_input
    )

    content = json.loads(response.content)
    assert (content is not None)
    assert (content['data'] is not None)
    assert (content['data']['updateCategory'] is not None)
    assert (content['data']['updateCategory']['category'] is not None)

    category = content['data']['updateCategory']['category']
    assert (category is not None)
    assert (category['id'] == '1')
    assert (category['name'] == 'test_category3')
