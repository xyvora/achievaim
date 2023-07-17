import pytest
from bson import ObjectId

from app.exceptions import NoRecordsUpdatedError
from app.models.user import UserUpdate, UserUpdateMe
from app.services.user_service import update_me, update_user


async def test_update_me_not_found():
    with pytest.raises(NoRecordsUpdatedError):
        await update_me(
            UserUpdateMe(
                id=ObjectId(),
                first_name="Imma",
                last_name="User",
                country="USA",
                password="test",
                user_name="test",
            )
        )


async def test_update_user_not_found():
    with pytest.raises(NoRecordsUpdatedError):
        await update_user(
            UserUpdate(
                id=ObjectId(),
                password="test",
                user_name="test",
                first_name="Some",
                last_name="Person",
                country="USA",
                is_active=True,
                is_admin=False,
            )
        )
