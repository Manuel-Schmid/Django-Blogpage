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
            success
          }
        }
        ''',
        variables=category_input
    )

    content = json.loads(response.content)
    assert content is not None
    assert content['data'] is not None
    data_create_category = content['data']['createCategory']
    assert data_create_category is not None
    assert data_create_category['category'] is not None
    assert data_create_category['success'] == True

    category = data_create_category['category']
    assert category is not None
    assert category['name'] == 'test_category4'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_category_too_long_fields(client_query):
    category_input = {
        "input": {
            "name": "e" * 201
        }
    }

    response = client_query(
        '''
        mutation CreateCategory($input: CategoryInput!) {
          createCategory(categoryInput: $input) {
            category {
              name
            }
            success
            errors
          }
        }
        ''',
        variables=category_input
    )

    content = json.loads(response.content)
    assert content is not None
    assert content['data'] is not None
    data_create_category = content['data']['createCategory']
    assert data_create_category is not None
    assert data_create_category['category'] is None
    assert data_create_category['success'] == False
    assert 'name' in data_create_category['errors']


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
            success
          }
        }
        ''',
        variables=category_input
    )

    content = json.loads(response.content)
    assert content is not None
    assert content['data'] is not None
    data_update_category = content['data']['updateCategory']
    assert data_update_category is not None
    assert data_update_category['category'] is not None
    assert data_update_category['success'] == True

    category = data_update_category['category']
    assert category is not None
    assert category['id'] == '1'
    assert category['name'] == 'test_category3'
