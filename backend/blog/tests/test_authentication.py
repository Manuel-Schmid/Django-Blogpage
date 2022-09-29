import json
import pytest
from django.core import mail


register_query = '''
        mutation Register($email: String!, $username: String!, $password1: String!, $password2: String!) {
          register(email: $email, username: $username, password1: $password1, password2: $password2) {
            success
            errors
            token
            refreshToken
          }
        }
        '''

verify_account_query = '''
        mutation VerifyAccount($token: String!) {
          verifyAccount(token: $token) {
            success
            errors
          }
        }
        '''


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_authentication(auth):
    content = json.loads(auth.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_token_auth = data.get('tokenAuth', None)
    assert data_token_auth is not None
    data_token = data_token_auth.get('token', None)
    assert data_token is not None


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_register(register, client_query):
    content = json.loads(register.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    register = data.get('register', None)
    assert register is not None
    success = register.get('success', None)
    assert success is True
    token = register.get('token', None)
    assert token is not None
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == ['admin@admin.com']


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_register_duplicate_email(register, client_query):
    signup_data = {
        "email": "admin@admin.com",
        "username": "abc",
        "password1": "helloWorld++x",
        "password2": "helloWorld++x"
    }

    response = client_query(register_query, variables=signup_data)
    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    register = data.get('register', None)
    assert register is not None
    success = register.get('success', None)
    assert success is False
    token = register.get('token', None)
    assert token is None
    assert len(mail.outbox) == 1


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_verify_account(register, client_query):
    register_content = json.loads(register.content)
    assert register_content is not None
    register_data = register_content.get('data', None)
    assert register_data is not None
    register = register_data.get('register', None)
    assert register is not None
    success = register.get('success', None)
    assert success is True
    token = register.get('token', None)
    assert token is not None

    token_obj = {
        "token": token,
    }

    response = client_query(verify_account_query, variables=token_obj)
    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    verify_account = data.get('verifyAccount', None)
    assert verify_account is not None
    success = verify_account.get('success', None)
    assert success is True


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_verify_invalid_token(client_query):
    token_obj = {
        "token": "test_token",
    }

    response = client_query(verify_account_query, variables=token_obj)
    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    verify_account = data.get('verifyAccount', None)
    assert verify_account is not None
    success = verify_account.get('success', None)
    assert success is False
