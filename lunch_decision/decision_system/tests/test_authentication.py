import json
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_signup_api_view():
    client = APIClient()

    User.objects.create_user(username='testuser', password='testpass')
    client.login(username='testuser', password='testpass')

    data = {
        'username': 'valery123',
        'password': 'pas1234',
    }

    response = client.post('/signup/', data, format='json')

    assert response.status_code == status.HTTP_200_OK

