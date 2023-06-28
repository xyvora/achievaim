from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from pymongo.errors import OperationFailure
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from app.api.deps import logger
from app.config import V1_API_PREFIX
from app.models.goals import Goal, GoalBase, GoalUpdate
from app.utils import APIRouter

router = APIRouter(tags=["Goal"], prefix=f"{V1_API_PREFIX}/goal")


@router.get("/")
async def get_goals() -> list[Goal]:
    """Get saved goals."""
    logger.info("Getting goals")
    return await Goal.find_all().to_list()


@router.get("/{db_id}")
async def get_goal_by_id(db_id: str) -> Goal:
    """Get a goal by database ID."""
    try:
        oid = ObjectId(db_id)
    except InvalidId:
        logger.info(f"{db_id} is not a valid ObjectId")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{db_id} is not a valid ID format"
        )
    goal_in_db = await Goal.find_one(Goal.id == oid)

    if not goal_in_db:
        logger.info(f"Goal with ID {db_id} not found")
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")

    return goal_in_db


@router.get("/name/{goal_name}")
async def get_goal_by_name(goal_name: str) -> Goal:
    """Get a goal by name."""
    goal_in_db = await Goal.find_one(Goal.name == goal_name)

    if not goal_in_db:
        logger.info(f"Goal with name {goal_name} not found")
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")

    return goal_in_db


@router.post("/")
async def create_goal(goal: GoalBase) -> Goal:
    """Add a new goal."""
    logger.info("Saving goal")
    try:
        db_goal = Goal(**goal.dict())
        saved_goal = await db_goal.insert()
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
    except Exception as e:
        logger.error(f"An error occurred while adding the goal: {e}")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="An error occurred while adding the goal",
        )

    return saved_goal


@router.delete("/{db_id}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_goal(db_id: str) -> None:
    """Delete a goal by database ID."""
    try:
        oid = ObjectId(db_id)
    except InvalidId:
        logger.info(f"{db_id} is not a valid ObjectId")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=f"{db_id} is not a valid ID format"
        )
    goal_in_db = await Goal.find_one(Goal.id == oid)

    if not goal_in_db:
        logger.info(f"Goal with ID {db_id} not found")
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")

    logger.info(f"Deleting goal with ID {db_id}")
    await goal_in_db.delete()


@router.delete("/name/{goal_name}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_goal_by_name(goal_name: str) -> None:
    """Delete a goal by name."""
    goal_in_db = await Goal.find_one(Goal.name == goal_name)

    if not goal_in_db:
        logger.info(f"Goal with name {goal_name} not found")
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")

    logger.info(f"Deleting goal {goal_name}")
    await goal_in_db.delete()


@router.put("/")
async def update_goal(goal: GoalUpdate) -> Goal:
    """Update a goal's information."""
    logger.info("Updating goal")
    try:
        oid = ObjectId(goal.id)
    except InvalidId:
        logger.info(f"{goal.id} is not a valid ObjectId")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"{goal.id} is not a valid ID format",
        )
    goal_in_db = await Goal.find_one(Goal.id == oid)

    if not goal_in_db:
        logger.info("Goal not found")
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Goal not found")

    update_data = goal.dict()
    update_data.pop("id", None)

    await goal_in_db.update({"$set": update_data})
    updated_goal = await Goal.find_one(Goal.id == oid)

    if not updated_goal:
        logger.info("An error occurred while updating the goal")
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="An error occurred while updating the goal",
        )

    return updated_goal
