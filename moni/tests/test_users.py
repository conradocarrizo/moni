import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    )

    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert user.password == 'testpassword'