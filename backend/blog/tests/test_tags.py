import json
import pytest


get_all_tags_query = '''
        {
          tags {
            name
            slug
          }
        }
        '''

get_used_tags_query = '''
         {
          usedTags {
            name
            slug
          }
        }
        '''


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_tags(tags):
    assert len(tags) == 3


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_get_all_tags(client_query, tags):
    response = client_query(get_all_tags_query)
    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_all_tags = data.get('tags', None)
    assert data_all_tags is not None
    assert len(data_all_tags) == 3


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_get_used_tags(client_query, tags):
    response = client_query(get_used_tags_query)
    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_used_tags = data.get('usedTags', None)
    assert data_used_tags is not None
    assert len(data_used_tags) == 2
