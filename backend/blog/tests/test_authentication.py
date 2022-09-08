import json
import pytest


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
