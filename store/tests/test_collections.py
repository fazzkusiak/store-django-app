from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self):
        
        client = APIClient()
        response = client.post('/shop/collection/', {'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED