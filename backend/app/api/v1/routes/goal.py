from uuid import uuid4

from bson.errors import InvalidId
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError, OperationFailure
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from app.api.deps import logger
from app.core.config import config
from app.models.user import Goal, GoalCreate, GoalWithUserId, User
from app.utils import APIRouter, str_to_oid

router = APIRouter(tags=["Goal"], prefix=f"{config.V1_API_PREFIX}/goal")


@router.get("/{user_id}")
async def get_user_goals(user_id: str) -> list[Goal]:
    """Get goals for a user."""
    logger.info("Getting goals")
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

    if not user.goals:
        logger.info("No goals found for user %s", user_id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No goals found for user {user_id}"
        )

    return user.goals


@router.get("/{user_id}/{goal_name}")
async def get_goal_by_name(user_id: str, goal_name: str) -> Goal:
    """Get a specifiic goal."""
    try:
        oid = str_to_oid(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{user_id} is not a valid ID format"
        )

    user = await User.find_one(User.id == oid)

    if not user:
        logger.info("User %s not found", user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    if not user.goals:
        logger.info("No goals found for user %s", user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No goals found for user")

    for goal in user.goals:
        if goal.name == goal_name:
            return goal

    logger.info("No goal named %s found for user %s", goal_name, user_id)
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND, detail=f"No goal named {goal_name} found for user {user_id}"
    )


@router.post("/")
async def create_goal(goal: GoalCreate) -> list[Goal]:
    """Add a new goal."""
    logger.info("Retrieving user %s", goal.user_id)
    user = await User.find_one(User.id == goal.user_id)

    if not user:
        logger.info("User with ID %s not found", goal.user_id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="User with ID {goal.user_id} not found"
        )

    _validate_unique_goal(user, goal.name)

    logger.info("Saving goal")
    goal_dict = goal.dict()
    goal_dict.pop("user_id")
    goal_dict["id"] = str(uuid4())
    db_goal = Goal(**goal_dict)
    if not user.goals:
        user.goals = [db_goal]
    else:
        user.goals.append(db_goal)
    try:
        await user.set({User.goals: user.goals})
    except DuplicateKeyError:
        logger.error("Goal already exists")
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal already exists")
    except OperationFailure as e:
        if e.code == 11000:  # Unique key violation
            logger.error("Goal already exists")
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal already exists")
        else:
            logger.error(f"An error occurred while adding the goal: {e}")
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="An error occurred while adding the goal",
            )
    except ValueError as e:
        if "Goal IDs must be unique" in str(e):
            logger.info("Goal IDs must be unique: %s", e)
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal IDs must be unique")
        if "Goal names must be unique" in str(e):
            logger.info("Goal names must be unique: %s", e)
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="Goal names must be unique"
            )
        logger.info("An error occurred %s", e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while adding the goal",
        )
    except Exception as e:
        logger.error("An error occurred while adding the goal: %s", e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while adding the goal",
        )

    updated_user = await User.find_one(User.id == user.id)

    if not updated_user or not updated_user.goals:
        logger.info("No goal inserted")
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Error inserting goal"
        )

    return updated_user.goals


@router.delete("/{user_id}/{goal_id}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_goal(user_id: str, goal_id: str) -> None:
    """Delete a user's goal by ID."""
    try:
        oid = str_to_oid(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{user_id} is not a valid ID format"
        )

    user = await User.find_one(User.id == oid)

    if not user:
        logger.info("User %s not found", user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    if not user.goals:
        logger.info("No goals found for user %s", user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No goals found for user")

    updated_goals = [x for x in user.goals if x.id != goal_id]
    if len(user.goals) == len(updated_goals):
        logger.info("Goal %s not found", goal_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"Goal {goal_id} not found")

    logger.info("Deleting goal %s for user %s", goal_id, user_id)
    await user.set({User.goals: updated_goals})


@router.delete(
    "/{user_id}/goal-name/{goal_name}", response_model=None, status_code=HTTP_204_NO_CONTENT
)
async def delete_goal_by_name(user_id: str, goal_name: str) -> None:
    """Delete a user's goal by name."""
    try:
        oid = str_to_oid(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{user_id} is not a valid ID format"
        )

    user = await User.find_one(User.id == oid)

    if not user:
        logger.info("User %s not found", user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    if not user.goals:
        logger.info("No goals found for user %s", user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No goals found for user")

    updated_goals = [x for x in user.goals if x.name != goal_name]
    if len(user.goals) == len(updated_goals):
        logger.info("Goal %s not found", goal_name)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"Goal {goal_name} not found")

    logger.info("Deleting goal %s for user %s", goal_name, user_id)
    await user.set({User.goals: updated_goals})


@router.put("/")
async def update_goal(goal: GoalWithUserId) -> Goal:
    """Update a goal's information."""
    logger.info("Retrieving user %s", goal.user_id)
    user = await User.find_one(User.id == goal.user_id)

    _validate_unique_goal(user, goal.name, goal.id)

    if not user:
        logger.info("User with ID %s not found", goal.user_id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="User with ID {goal.user_id} not found"
        )

    if not user.goals:
        logger.info("No goals found for user %s", goal.user_id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No goals found for user {goal.user_id}"
        )

    logger.info("Updating goal")
    goal_dict = goal.dict()
    goal_dict.pop("user_id")

    for i, user_goal in enumerate(user.goals):
        if user_goal.id == goal.id:
            db_goal = Goal(**goal_dict)
            user.goals[i] = db_goal
            try:
                await user.set({User.goals: user.goals})
            except DuplicateKeyError:
                logger.error("Goal already exists")
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal already exists")
            except OperationFailure as e:
                if e.code == 11000:  # Unique key violation
                    logger.error("Goal already exists")
                    raise HTTPException(
                        status_code=HTTP_400_BAD_REQUEST, detail="Goal already exists"
                    )
                else:
                    logger.error(f"An error occurred while adding the goal: {e}")
                    raise HTTPException(
                        status_code=HTTP_400_BAD_REQUEST,
                        detail="An error occurred while adding the goal",
                    )
            except Exception as e:
                logger.error(f"An error occurred while adding the goal: {e}")
                raise HTTPException(
                    status_code=HTTP_400_BAD_REQUEST,
                    detail="An error occurred while adding the goal",
                )

            return db_goal

    logger.info("Goal %s not found for user %s", goal.id, goal.user_id)
    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND, detail=f"Goal {goal.id} not found for user {goal.user_id}"
    )


def _validate_unique_goal(user: User, goal_name: str, goal_id: str | None = None) -> None:
    if not user.goals:
        return None

    if goal_name in [x.name for x in user.goals]:
        logger.info("Goal names must be unique")
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal names must be unique")

    if goal_id and goal_id in [x.id for x in user.goals]:
        logger.info("Goal IDs must be unique")
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal IDs must be unique")

    return None
