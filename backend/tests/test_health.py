import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_health_check_reports_application_and_database_health(client):
    response = client.get(reverse("health-check"))
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "database": "connected"}
