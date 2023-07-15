from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from app.api.deps import Config, CurrentUser, logger
from app.core.config import config
from app.core.security import create_access_token, verify_password
from app.core.utils import APIRouter
from app.models.token import Token
from app.models.user import UserNoPassword
from app.services.user_service import get_full_user_by_username

router = APIRouter(tags=["Login"], prefix=f"{config.V1_API_PREFIX}/login")


@router.post("/access-token")
async def login_access_token(
    config: Config, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """OAuth2 compatible token login, get an access token for future requests."""

    logger.info("Logging user in.")
    user = await get_full_user_by_username(form_data.username)

    if not user:
        logger.info("Incorrect user name")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Incorrect user name or password"
        )

    if not user.is_active:
        logger.info("Inactive user")
        raise HTTPException(status_code=400, detail="Inactive user")

    # This shouldn't be possible to hit by mypy wants the check just in case
    if not user.id:  # pragma: no cover
        logger.info("User ID is missing")
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="User Id is missing")

    if not verify_password(form_data.password, user.hashed_password):
        logger.info("Incorrect password")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Incorrect user name or password"
        )

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)

    token = Token(
        access_token=create_access_token(user.id, expires_delta=access_token_expires),
        token_type="Bearer",
    )

    return token


@router.post("/test-token")
def test_token(current_user: CurrentUser) -> UserNoPassword:
    """Test access token."""
    return UserNoPassword(**current_user.dict())
