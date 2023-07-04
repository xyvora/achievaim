# from app.core.config import config
from app.core.security import (
    get_password_hash,
    pwd_context,
    verify_password,
)


def test_verify_password_match():
    password = "test"
    hashed = pwd_context.hash(password)

    assert verify_password(password, hashed)


def test_verify_password_mismatch():
    password = "test"
    hashed = pwd_context.hash("bad")

    assert not verify_password(password, hashed)


def test_get_password_hash():
    password = "test"

    assert get_password_hash(password) != password


# @pytest.mark.parametrize(
#     "expires_delta",
#     [
#         timedelta(minutes=5),
#         timedelta(minutes=10),
#     ],
# )
# def test_create_access_token_expire(expires_delta):
#     data = {"email": "test@user.com", "is_active": True}
#     exp = timegm((datetime.utcnow() + expires_delta).utctimetuple())
#     token = create_access_token(data, expires_delta=expires_delta)
#
#     expected = {"email": "test@user.com", "is_active": True, "exp": exp}
#     decoded = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
#
#     assert decoded == expected
#
#
# def test_create_access_token_expire_none():
#     data = {"email": "test@user.com", "is_active": True}
#     exp = timegm((datetime.now(tz=UTC) + timedelta(minutes=15)).utctimetuple())
#     token = create_access_token(data)
#
#     expected = {"email": "test@user.com", "is_active": True, "exp": exp}
#     decoded = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
#
#     assert decoded == expected
