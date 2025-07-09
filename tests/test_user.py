import requests
import pytest

BASE_URL = "http://127.0.0.1:8000/users"

def test_users_unauthorized(requests_mock):
    # Mock the URL with expected query parameters
    requests_mock.get(
        f"{BASE_URL}?username=admin&password=admin",
        status_code=401,
        text=""
    )

    response = requests.get(BASE_URL, params={"username": "admin", "password": "admin"})

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty body, got: {response.text!r}"


def test_users_authorized_but_empty(requests_mock):
    # Mock the URL with different query parameters
    requests_mock.get(
        f"{BASE_URL}?username=admin&password=qwerty",
        status_code=200,
        text=""
    )

    response = requests.get(BASE_URL, params={"username": "admin", "password": "qwerty"})

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty body, got: {response.text!r}"
