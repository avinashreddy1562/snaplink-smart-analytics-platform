import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_custom_user_model_persists_required_account_fields():
    user = get_user_model().objects.create_user(
        username="avinash", email="avinash@example.com", password="not-a-real-password"
    )
    assert user.email == "avinash@example.com"
    assert user.created_at is not None
    assert user.updated_at is not None
    assert user.check_password("not-a-real-password")
