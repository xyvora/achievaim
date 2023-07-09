from datetime import timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from app.api.deps import Config, CurrentUser, logger
from app.core.config import config
from app.core.security import create_access_token, get_password_hash
from app.core.utils import APIRouter
from app.models.token import Token
from app.models.user import User, UserNoPassword

router = APIRouter(tags=["Login"], prefix=f"{config.V1_API_PREFIX}/goal")


@router.post("/login/access-token")
async def login_access_token(
    config: Config, form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    """OAuth2 compatible token login, get an access token for future requests."""
    logger.info("Logging user in.")
    hashed_password = get_password_hash(form_data.password)
    user = await User.find_one(
        User.user_name == form_data.username, hashed_password=hashed_password
    )
    if not user:
        logger.info("Incorrect user name or password")
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    elif not user.is_active:
        logger.info("Inactive user")
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)

    # This shouldn't be possible to hit by mypy wants the check just in case
    if not user.id:  # pragma: no cover
        logger.info("User ID is missing")
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="User Id is missing")

    return Token(
        access_token=create_access_token(user.id, expires_delta=access_token_expires),
        token_type="bearer",
    )


@router.post("/login/test-token")
def test_token(current_user: CurrentUser) -> UserNoPassword:
    """Test access token."""
    return current_user
