from bson.errors import InvalidId
from fastapi import HTTPException
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from app.api.deps import logger
from app.core.config import config
from app.models.user import Goal, User
from app.utils import APIRouter, str_to_oid

router = APIRouter(tags=["Goal"], prefix=f"{config.V1_API_PREFIX}/goal")


@router.get("/{user_id}")
async def get_user_by_id(user_id: str) -> list[Goal]:
    """Get saved goals for a user."""
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

    return user.goals


@router.get("/{user_id}/{goal_name}")
async def get_goal_by_name(user_id: str, goal_name: str) -> Goal:
    """Get a goal by name."""
    try:
        oid = str_to_oid(user_id)
    except InvalidId:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{user_id} is not a valid ID format"
        )

    goal = await User.find_one(User.id == oid, Goal.name == goal_name)

    if not goal:
        logger.info("Goal with name %s not found for user %s", goal_name, user_id)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")

    return goal


# @router.post("/")
# async def create_goal(goal: GoalBase) -> Goal:
#     """Add a new goal."""
#     logger.info("Saving goal")
#     try:
#         db_goal = Goal(**goal.dict())
#         saved_goal = await db_goal.insert()
#     except OperationFailure as e:
#         if e.code == 11000:  # Unique key violation
#             logger.error("Goal already exists")
#             raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Goal already exists")
#         else:
#             logger.error(f"An error occurred while adding the goal: {e}")
#             raise HTTPException(
#                 status_code=HTTP_400_BAD_REQUEST,
#                 detail="An error occurred while adding the goal",
#             )
#     except Exception as e:
#         logger.error(f"An error occurred while adding the goal: {e}")
#         raise HTTPException(
#             status_code=HTTP_400_BAD_REQUEST,
#             detail="An error occurred while adding the goal",
#         )
#
#     return saved_goal
#
#
# @router.delete("/{db_id}", response_model=None, status_code=HTTP_204_NO_CONTENT)
# async def delete_goal(db_id: str) -> None:
#     """Delete a goal by database ID."""
#     try:
#         oid = ObjectId(db_id)
#     except InvalidId:
#         logger.info(f"{db_id} is not a valid ObjectId")
#         raise HTTPException(
#             status_code=HTTP_400_BAD_REQUEST, detail=f"{db_id} is not a valid ID format"
#         )
#     goal_in_db = await Goal.find_one(Goal.id == oid)
#
#     if not goal_in_db:
#         logger.info(f"Goal with ID {db_id} not found")
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")
#
#     logger.info(f"Deleting goal with ID {db_id}")
#     await goal_in_db.delete()
#
#
# @router.delete("/name/{goal_name}", response_model=None, status_code=HTTP_204_NO_CONTENT)
# async def delete_goal_by_name(goal_name: str) -> None:
#     """Delete a goal by name."""
#     goal_in_db = await Goal.find_one(Goal.name == goal_name)
#
#     if not goal_in_db:
#         logger.info(f"Goal with name {goal_name} not found")
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")
#
#     logger.info(f"Deleting goal {goal_name}")
#     await goal_in_db.delete()
#
#
# @router.put("/")
# async def update_goal(goal: GoalUpdate) -> Goal:
#     """Update a goal's information."""
#     logger.info("Updating goal")
#     try:
#         oid = ObjectId(goal.id)
#     except InvalidId:
#         logger.info(f"{goal.id} is not a valid ObjectId")
#         raise HTTPException(
#             status_code=HTTP_400_BAD_REQUEST,
#             detail=f"{goal.id} is not a valid ID format",
#         )
#     goal_in_db = await Goal.find_one(Goal.id == oid)
#
#     if not goal_in_db:
#         logger.info("Goal not found")
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")
#
#     update_data = goal.dict()
#     update_data.pop("id", None)
#
#     await goal_in_db.update({"$set": update_data})
#     updated_goal = await Goal.find_one(Goal.id == oid)
#
#     if not updated_goal:
#         logger.info("An error occurred while updating the goal")
#         raise HTTPException(
#             status_code=HTTP_400_BAD_REQUEST,
#             detail="An error occurred while updating the goal",
#         )
#
#     return updated_goal
