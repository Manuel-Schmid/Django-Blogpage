import json
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_categories(categories):
    assert len(categories) == 2


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_category(client_query):
    category_input = {
        "input": {
            "name": "test_category4",
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
    data = content.get('data', None)
    assert data is not None
    data_create_category = data.get('createCategory', None)
    assert data_create_category is not None
    assert data_create_category['success'] is True
    data_category = data_create_category.get('category', None)
    assert data_category is not None
    assert data_category['name'] == 'test_category4'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_category_too_long_fields(client_query):
    category_input = {
        "input": {
            "name": "e" * 201,
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
    data = content.get('data', None)
    assert data is not None
    data_create_category = data.get('createCategory', None)
    assert data_create_category is not None
    assert data_create_category['success'] is False
    data_category = data_create_category.get('category', None)
    assert data_category is None
    assert 'name' in data_create_category['errors']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_category(client_query, categories):
    category_input = {
        "input": {
            "id": 1,
            "name": "test_category3",
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
    data = content.get('data', None)
    assert data is not None
    data_update_category = data.get('updateCategory', None)
    assert data_update_category is not None
    assert data_update_category['success'] is True
    data_category = data_update_category.get('category', None)
    assert data_category is not None
    assert data_category['id'] == '1'
    assert data_category['name'] == 'test_category3'
