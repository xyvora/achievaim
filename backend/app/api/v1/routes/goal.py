from bson import ObjectId
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError, OperationFailure
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from app.api.deps import CurrentUser, logger
from app.core.config import config
from app.core.utils import APIRouter
from app.exceptions import DuplicateGoalError
from app.models.user import Goal, GoalCreate, User
from app.services.goal_service import create_goal as create_goal_service
from app.services.goal_service import get_goal_by_id as get_goal_by_id_service
from app.services.goal_service import get_goal_by_name as get_goal_by_name_service
from app.services.goal_service import get_goals_by_user_id
from app.services.user_service import get_full_user

router = APIRouter(tags=["Goal"], prefix=f"{config.V1_API_PREFIX}/goal")


@router.post("/")
async def create_goal(goal: GoalCreate, current_user: CurrentUser) -> list[Goal]:
    """Add a new goal."""
    logger.info("Creating goal for user %s", current_user.id)
    try:
        goals = await create_goal_service(ObjectId(current_user.id), goal)
    except DuplicateGoalError:
        logger.error("Goal with the name %s already exists for user %s", goal.name, current_user.id)
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Goal with the name {goal.name} already exists",
        )
    except ValueError as e:  # pragma: no cover
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
    except Exception as e:  # pragma: no cover
        logger.error("An error occurred while adding the goal: %s", e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while adding the goal",
        )

    return goals


@router.delete("/{goal_id}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_goal(goal_id: str, current_user: CurrentUser) -> None:
    """Delete a user's goal by ID."""
    user = await get_full_user(ObjectId(current_user.id))

    if not user:  # pragma: no cover
        logger.info("No user found with id %s", current_user.id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No user found with id {current_user.id}"
        )

    if not user.goals:
        logger.info("No goals found for user %s", current_user.id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No goals found for user")

    updated_goals = [x for x in user.goals if x.id != goal_id]
    if len(user.goals) == len(updated_goals):
        logger.info("Goal %s not found", goal_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"Goal {goal_id} not found")

    logger.info("Deleting goal %s for user %s", goal_id, current_user.id)
    await user.set({User.goals: updated_goals})


@router.delete("/goal-name/{goal_name}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_goal_by_name(goal_name: str, current_user: CurrentUser) -> None:
    """Delete a user's goal by name."""
    user = await get_full_user(ObjectId(current_user.id))

    if not user:  # pragma: no cover
        logger.info("No user found with id %s", current_user.id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No user found with id {current_user.id}"
        )

    if not user.goals:
        logger.info("No goals found for user %s", current_user.id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No goals found for user")

    updated_goals = [x for x in user.goals if x.name != goal_name]
    if len(user.goals) == len(updated_goals):
        logger.info("Goal %s not found", goal_name)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"Goal {goal_name} not found")

    logger.info("Deleting goal %s for user %s", goal_name, current_user.id)
    await user.set({User.goals: updated_goals})


@router.get("/")
async def get_user_goals(current_user: CurrentUser) -> list[Goal]:
    """Get goals for a user."""
    logger.info("Getting goals for user %s", current_user.id)
    goals = await get_goals_by_user_id(ObjectId(current_user.id))

    if not goals:
        logger.info("No goals found for user %s", current_user.id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No goals found for user {current_user.id}"
        )

    return goals


@router.get("/{goal_id}")
async def get_goal_by_id(goal_id: str, current_user: CurrentUser) -> Goal:
    """Get a specifiic goal by goal ID."""
    goal = await get_goal_by_id_service(ObjectId(current_user.id), goal_id)

    if not goal:
        logger.info("No goal named %s found for ID %s", goal_id, current_user.id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"No goal ID {goal_id} found")

    return goal


@router.get("/goal-name/{goal_name}")
async def get_goal_by_name(goal_name: str, current_user: CurrentUser) -> Goal:
    """Get a specifiic goal."""
    goal = await get_goal_by_name_service(ObjectId(current_user.id), goal_name)

    if not goal:
        logger.info("No goal named %s found for user %s", goal_name, current_user.id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No goal named {goal_name} found"
        )

    return goal


@router.put("/")
async def update_goal(goal: Goal, current_user: CurrentUser) -> Goal:
    """Update a goal's information."""
    user = await get_full_user(ObjectId(current_user.id))

    if not user:  # pragma: no cover
        logger.info("No user found with id %s", current_user.id)
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"No user found with id {current_user.id}"
        )

    _validate_unique_goal(user, goal.name)

    if not user.goals:
        logger.info("No goals found for user %s", current_user.id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No goals found for user")

    logger.info("Updating goal")
    goal_dict = goal.dict()

    for i, user_goal in enumerate(user.goals):
        if user_goal.id == goal.id:
            db_goal = Goal(**goal_dict)
            user.goals[i] = db_goal
            try:
                await user.set({User.goals: user.goals})
            except DuplicateKeyError:  # pragma: no cover
                logger.error("Goal already exists")
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal already exists")
            except OperationFailure as e:  # pragma: no cover
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
            except Exception as e:  # pragma: no cover
                logger.error(f"An error occurred while adding the goal: {e}")
                raise HTTPException(
                    status_code=HTTP_400_BAD_REQUEST,
                    detail="An error occurred while adding the goal",
                )

            return db_goal

    logger.info("Goal %s not found for user %s", goal.id, current_user.id)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"Goal {goal.id} not found")


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
