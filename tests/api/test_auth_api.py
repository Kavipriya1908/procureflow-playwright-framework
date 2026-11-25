import time

import pytest
from jsonschema import validate

from config import settings
from schemas.login_schema import LOGIN_SCHEMA


def test_wrong_password(auth_api):
    response = auth_api.login("qa.invalid.user@example.com", "WrongPass123")
    assert response.status == 401


def test_unknown_user(auth_api):
    response = auth_api.login("no.such.user@example.com", "Test@12345")
    assert response.status == 401


def test_sql_injection(auth_api):
    response = auth_api.login("' OR '1'='1", "anything")
    assert response.status in (400, 401)


@pytest.mark.needs_credentials
def test_valid_login(auth_api):
    response = auth_api.login(settings.VALID_EMAIL, settings.VALID_PASSWORD)
    assert response.status == 200


@pytest.mark.needs_credentials
def test_login_response_time(auth_api):
    start = time.perf_counter()
    response = auth_api.login(settings.VALID_EMAIL, settings.VALID_PASSWORD)
    seconds = time.perf_counter() - start

    assert response.status == 200
    assert seconds < 2


@pytest.mark.needs_credentials
def test_login_header(auth_api):
    response = auth_api.login(settings.VALID_EMAIL, settings.VALID_PASSWORD)

    assert "application/json" in response.headers["content-type"]


@pytest.mark.needs_credentials
def test_login_schema(auth_api):
    response = auth_api.login(settings.VALID_EMAIL, settings.VALID_PASSWORD)
    body = response.json()

    validate(instance=body, schema=LOGIN_SCHEMA)
