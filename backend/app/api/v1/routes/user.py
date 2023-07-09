from beanie.exceptions import RevisionIdWasChanged
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from app.api.deps import logger
from app.core.config import config
from app.core.security import get_password_hash
from app.core.utils import APIRouter, str_to_oid
from app.models.user import User, UserCreate, UserNoPassword, UserUpdate

router = APIRouter(tags=["User"], prefix=f"{config.V1_API_PREFIX}/user")


@router.post("/")
async def create_user(user: UserCreate) -> UserNoPassword:
    """Create a new user."""
    logger.info("Creating user")
    try:
        user.password = get_password_hash(user.password)
    except Exception as e:  # pragma: no cover
        logger.info("An error occurred while hashing the password: %s", e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while hasing the password",
        )

    try:
        user_dict = user.dict()
        user_dict["hashed_password"] = user_dict.pop("password")
        db_user = User(**user_dict)
        saved_user = await db_user.insert()
    except DuplicateKeyError as e:
        logger.info("User name %s already exists: %s", user.user_name, e)
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"A user with the user name {user.user_name} already exists",
        )
    except Exception as e:  # pragma: no cover
        logger.info("An error occurred while inserting user: %s", e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the user",
        )

    return UserNoPassword(**saved_user.dict())


@router.get("/")
async def get_users() -> list[UserNoPassword]:
    """Get all users."""
    logger.info("Getting all users")
    users = await User.find_all().to_list()

    if not users:
        logger.info("No users found")
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No users found")

    return [UserNoPassword(**x.dict()) for x in users]


@router.get("/{user_id}")
async def get_user_by_id(user_id: str) -> UserNoPassword:
    """Get a user by ID."""
    logger.info("Getting user %s", user_id)
    try:
        oid = str_to_oid(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{user_id} is not a valid ID format"
        )

    user = await User.find_one(User.id == oid)

    if not user:
        logger.info("User with id %s not found", user_id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found"
        )

    return UserNoPassword(**user.dict())


@router.get("/user-name/{user_name}")
async def get_user_by_user_name(user_name: str) -> UserNoPassword:
    """Get a user by user name."""
    logger.info("Getting user %s", user_name)
    user = await User.find_one(User.user_name == user_name)

    if not user:
        logger.info("User with user name %s not found", user_name)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"User with user name {user_name} not found"
        )

    return UserNoPassword(**user.dict())


@router.delete("/{user_id}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_user_by_id(user_id: str) -> None:
    """Delete a user by ID."""
    try:
        oid = ObjectId(user_id)
    except InvalidId:
        logger.info("%s is not a valid ObjectId", user_id)
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{user_id} is not a valid ID format"
        )
    user_in_db = await User.find_one(User.id == oid)

    if not user_in_db:
        logger.info("User with ID %s not found", user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    logger.info("Deleting user with ID %s", user_id)
    await user_in_db.delete()


@router.delete("/user-name/{user_name}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_user_by_user_name(user_name: str) -> None:
    """Delete a user by user name."""
    user_in_db = await User.find_one(User.user_name == user_name)

    if not user_in_db:
        logger.info("User with user name %s not found", user_name)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    logger.info("Deleting user with user name %s", user_name)
    await user_in_db.delete()


@router.put("/")
async def update_user(user: UserUpdate) -> UserNoPassword:
    """Update a user's information."""
    logger.info("Updating user")
    user_in_db = await User.find_one(User.id == user.id)

    if not user_in_db:
        logger.info("User not found")
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    update_user = user.dict()
    update_user["hashed_password"] = update_user.pop("password")
    db_user = User(**update_user)
    try:
        await user_in_db.update({"$set": db_user.dict()})
    except RevisionIdWasChanged as e:
        logger.info("User name %s already exists: %s", user.user_name, e)
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="User name {user.user_name} already exists"
        )
    except Exception as e:  # pragma: no cover
        logger.info("An error occurred while updating user %s: %s", user.id, e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updatingg user",
        )

    updated_user = await User.find_one(User.id == user.id)

    if not updated_user:  # pragma: no cover
        logger.info("An error occurred while updating the user")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="An error occurred while updating the user"
        )

    return UserNoPassword(**updated_user.dict())
