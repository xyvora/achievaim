from calendar import timegm
from datetime import UTC, datetime, timedelta

import jwt
import pytest
from passlib.hash import argon2

from app.core.config import config
from app.core.security import (
    ALGORITHM,
    DEFAULT_ROUNDS,
    create_access_token,
    get_password_hash,
    verify_password,
)


def test_verify_password_match():
    password = "test"
    hashed = argon2.using(rounds=DEFAULT_ROUNDS).hash(password)

    assert verify_password(password, hashed)


def test_verify_password_mismatch():
    password = "test"
    hashed = argon2.using(rounds=DEFAULT_ROUNDS).hash("bad")

    assert not verify_password(password, hashed)


def test_get_password_hash():
    password = "test"

    assert get_password_hash(password) != password


@pytest.mark.parametrize(
    "expires_delta",
    [
        timedelta(minutes=5),
        timedelta(minutes=10),
    ],
)
def test_create_access_token_expire(expires_delta):
    data = {"id": "someid", "is_active": True}
    exp = timegm((datetime.now(tz=UTC) + expires_delta).utctimetuple())
    token = create_access_token(data, expires_delta=expires_delta)

    expected = {"exp": exp, "sub": "{'id': 'someid', 'is_active': True}"}
    decoded = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded == expected


def test_create_access_token_expire_none():
    data = {"id": "someid", "is_active": True}
    token = create_access_token(data)

    expected = "{'id': 'someid', 'is_active': True}"
    decoded = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])

    assert "exp" in decoded
    assert "sub" in decoded
    assert decoded["sub"] == expected
