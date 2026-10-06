import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "application")
    )
)

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"DevOps Flask App" in response.data


def test_health_check():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.data == b"Application is healthy!"