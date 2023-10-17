import pytest
from myapp.models import MyUser

@pytest.fixture
def user():
    return MyUser.objects.create(is_active=True)

@pytest.mark.django_db
def test_deactivate(user):
    user.deactivate()
    assert not user.is_active

@pytest.mark.django_db
def test_deactivate_activate(user):
    user.deactivate()
    user.activate()
    assert user. is_active
    