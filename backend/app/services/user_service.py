from datetime import datetime

from beanie import PydanticObjectId
from beanie.odm.operators.update.general import Set
from bson import ObjectId

from app.core.security import get_password_hash
from app.exceptions import (
    DuplicateUserNameError,
    NoRecordsDeletedError,
    NoRecordsUpdatedError,
    UserNotFoundError,
)
from app.models.user import User, UserCreate, UserNoGoals, UserNoPassword, UserUpdate, UserUpdateMe


async def create_user(user: UserCreate) -> UserNoPassword:
    user_name = user.user_name.lower().strip()

    if await get_user_by_user_name(user_name):
        raise DuplicateUserNameError(f"A user with the user name {user.user_name} already exists")

    first_name = user.first_name.strip()
    last_name = user.last_name.strip()
    if user.country:
        country = user.country.strip()
    hashed_password = get_password_hash(user.password)
    user = User(
        user_name=user_name,
        first_name=first_name,
        last_name=last_name,
        country=country,
        avatar_url=user.avatar_url,
        hashed_password=hashed_password,
    )
    await user.save()

    updated_user = await User.find_one(User.id == user.id, projection_model=UserNoPassword)

    if not updated_user:  # pragma: no cover
        raise UserNotFoundError("User not found after update")

    return updated_user


async def delete_user_by_id(user_id: ObjectId | PydanticObjectId) -> None:
    delete_result = await User.find_one(User.id == user_id).delete()

    if not delete_result or delete_result.deleted_count < 1:
        raise NoRecordsDeletedError(f"User with id {user_id} not found")


async def delete_user_by_user_name(user_name: str) -> None:
    delete_result = await User.find_one(User.user_name == user_name.lower().strip()).delete()

    if not delete_result or delete_result.deleted_count < 1:
        raise NoRecordsDeletedError(f"User with user name {user_name} not found")


async def get_full_user(user_id: ObjectId | PydanticObjectId) -> User | None:
    return await User.find_one(User.id == user_id)


async def get_full_user_by_username(user_name: str) -> User | None:
    return await User.find_one(User.user_name == user_name.lower().strip())


async def get_user_by_id(user_id: ObjectId | PydanticObjectId) -> UserNoPassword | None:
    return await User.find_one(User.id == user_id, projection_model=UserNoPassword)


async def get_user_by_user_name(user_name: str) -> UserNoPassword | None:
    return await User.find_one(
        User.user_name == user_name.lower().strip(), projection_model=UserNoPassword
    )


async def get_user_no_goal(user_id: ObjectId | PydanticObjectId) -> UserNoGoals | None:
    return await User.find_one(User.id == user_id, projection_model=UserNoGoals)


async def get_users() -> list[UserNoPassword]:
    users = await User.find_all().to_list()
    return [UserNoPassword(**x.dict()) for x in users]


async def update_me(update_info: UserUpdateMe) -> UserNoPassword:
    user_name = update_info.user_name.lower().strip()
    first_name = update_info.first_name.strip()
    last_name = update_info.last_name.strip()
    country = update_info.country.strip()
    password = update_info.password.strip()
    hashed_password = get_password_hash(password)
    update_result = await User.find_one(User.id == update_info.id).update(
        Set(
            {
                User.user_name: user_name,
                User.first_name: first_name,
                User.last_name: last_name,
                User.country: country,
                User.avatar_url: update_info.avatar_url,
                User.hashed_password: hashed_password,
                User.last_update: datetime.now(),
            }
        )
    )

    if update_result.modified_count < 1:
        raise NoRecordsUpdatedError(f"Error updating user {update_info.id}")

    updated_user = await User.find_one(User.id == update_info.id, projection_model=UserNoPassword)

    if not updated_user:  # pragma: no cover
        raise UserNotFoundError("User not found after update")

    return updated_user


async def update_user(update_info: UserUpdate) -> UserNoPassword:
    user_name = update_info.user_name.lower().strip()
    first_name = update_info.first_name.strip()
    last_name = update_info.last_name.strip()
    country = update_info.country.strip()
    password = update_info.password.strip()
    hashed_password = get_password_hash(password)
    update_result = await User.find_one(User.id == update_info.id).update(
        Set(
            {
                User.user_name: user_name,
                User.first_name: first_name,
                User.last_name: last_name,
                User.country: country,
                User.avatar_url: update_info.avatar_url,
                User.hashed_password: hashed_password,
                User.last_update: datetime.now(),
                User.is_active: update_info.is_active,
                User.is_admin: update_info.is_admin,
            }
        )
    )

    if update_result.modified_count < 1:
        raise NoRecordsUpdatedError(f"Error updating user {update_info.id}")

    updated_user = await User.find_one(User.id == update_info.id, projection_model=UserNoPassword)

    if not updated_user:  # pragma: no cover
        raise UserNotFoundError("User not found after update")

    return updated_user
