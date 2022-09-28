import json
import pytest


update_user_email_query = '''
        mutation UpdateUserEmail($newEmail: String!) {
          updateUserEmail(newEmail: $newEmail) {
            success
            user {
              email
            }
          }
        }
        '''


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_user_email(auth, client_query):
    variables = {
        "newEmail": "user3@example.com"
    }

    response = client_query(update_user_email_query, variables=variables)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_update_user_email = data.get('updateUserEmail', None)
    assert data_update_user_email is not None

    success = data_update_user_email.get('success', None)
    assert success is not None
    assert success

    user = data_update_user_email.get('user', None)
    assert user is not None
    email = user.get('email', None)
    assert email is not None
    assert email == 'user3@example.com'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_update_user_email_unauthenticated(users, client_query):
    variables = {
        "newEmail": "user3@example.com"
    }

    response = client_query(update_user_email_query, variables=variables)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_update_user_email = data.get('updateUserEmail', None)
    assert data_update_user_email is not None

    success = data_update_user_email.get('success', None)
    assert success is not None
    assert success is False
