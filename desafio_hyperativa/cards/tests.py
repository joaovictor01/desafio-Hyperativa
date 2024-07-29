import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Card

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
@pytest.mark.django_db(True)
def create_user():
    user = User.objects.create_user(username="testuser", password="testpassword")
    return user


@pytest.fixture
@pytest.mark.django_db(True)
def create_card():
    return Card.objects.create(name="Test Card", card_number="4456897999999999")


@pytest.mark.django_db(True)
def test_register_user(api_client):
    url = reverse("register")
    data = {
        "username": "testuser",
        "password": "testpassword",
        "email": "test@example.com",
    }
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db(True)
def test_login_user(api_client, create_user):
    url = reverse("token_obtain_pair")
    data = {"username": "testuser", "password": "testpassword"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db(True)
def test_add_card(api_client, create_user):
    api_client.login(username="testuser", password="testpassword")
    user = User.objects.first()
    api_client.force_authenticate(user=user)
    url = reverse("add_card")
    data = {"name": "Test Card", "card_number": "4456897999999999"}
    response = api_client.post(
        url,
        data,
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db(True)
def test_get_card_by_number(api_client, create_user, create_card):
    api_client.login(username="testuser", password="testpassword")
    user = User.objects.first()
    api_client.force_authenticate(user=user)
    url = reverse("get_card_by_number", args=["4456897999999999"])
    response = api_client.get(
        url,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == create_card.id
