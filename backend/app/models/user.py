from enum import Enum

from beanie import Document, Indexed
from bson import ObjectId
from camel_converter.pydantic_base import CamelBase
from pydantic import validator

from app.models.object_id import ObjectIdStr


class RepeatsEvery(str, Enum):
    day = "day"
    week = "week"
    month = "month"


class DaysOfWeek(CamelBase):
    monday: bool = False
    tuesday: bool = False
    wednesday: bool = False
    thursday: bool = False
    friday: bool = False
    saturday: bool = False
    sunday: bool = False


class _GoalBase(CamelBase):
    name: str
    duration: int
    days_of_week: DaysOfWeek
    repeats_every: RepeatsEvery
    progress: float


class Goal(_GoalBase):
    id: str


class GoalCreate(_GoalBase):
    pass


class GoalWithUserId(Goal):
    user_id: ObjectIdStr

    class Config:
        json_encoders = {ObjectId: lambda x: str(x)}


class UserCreate(CamelBase):
    user_name: str
    password: str


class UserNoPassword(CamelBase):
    id: ObjectIdStr
    user_name: str
    goals: list[Goal] | None = None

    class Config:
        json_encoders = {ObjectId: lambda x: str(x)}


class UserUpdate(CamelBase):
    id: ObjectIdStr
    password: str
    user_name: str

    class Config:
        json_encoders = {ObjectId: lambda x: str(x)}


class User(Document):
    user_name: Indexed(str, unique=True)  # type: ignore
    hashed_password: str
    goals: list[Goal] | None = None
    is_active: bool = True
    is_admin: bool = False

    class Settings:
        name = "users"

    @validator("goals")
    @classmethod
    def validate_goals(cls, v: list[Goal] | None) -> list[Goal] | None:
        """Validate that the goal names and ids are unique.

        I want this to happen in the database, but so far I haven't been able to get Beanie to do it.
        """
        if not v:
            return None

        goal_ids = {x.id for x in v}
        if len(v) != len(goal_ids):
            raise ValueError(
                "Goal IDs must be unique",
            )

        goal_names = {x.name for x in v}
        if len(v) != len(goal_names):
            raise ValueError(
                "Goal names must be unique",
            )

        return v
