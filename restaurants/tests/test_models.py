import os
import pytest
import django

from django.contrib.auth import get_user_model
from django.utils import timezone
from restaurants.models import Restaurant, Menu, Vote

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lunch_decision_core.settings")

django.setup()


@pytest.fixture
def restaurant():
    return Restaurant.objects.create(
        name="Test Restaurant", address="Test Address", contact_info="Test Contact"
    )


@pytest.fixture
def menu(restaurant):
    return Menu.objects.create(
        restaurant=restaurant,
        date=timezone.now().date(),
        menu_detail={
            "starter": "Salad",
            "main": "Steak",
            "dessert": "Ice Cream"
        },
        vote_count=0,
    )


@pytest.fixture
def user():
    user = get_user_model()
    return user.objects.create_user(
        email="user@example.com", password="password"
    )


@pytest.fixture
def vote(menu, user):
    return Vote.objects.create(employee=user, menu=menu)


@pytest.mark.django_db
def test_restaurant_str(restaurant):
    assert str(restaurant) == "Test Restaurant"


@pytest.mark.django_db
def test_menu_str(menu):
    result_str = f"Menu for {timezone.now().date()} - Test Restaurant"
    assert str(menu) == result_str


@pytest.mark.django_db
def test_vote_str(vote):
    result_str = (
        f"Vote by user@example.com for Menu for"
        f" {timezone.now().date()} - Test Restaurant"
    )
    assert str(vote) == result_str
