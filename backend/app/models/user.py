from enum import Enum

from beanie import Document, Indexed
from bson import ObjectId
from camel_converter import to_camel
from camel_converter.pydantic_base import CamelBase

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
    name: Indexed(str, unique=True)  # type: ignore[valid-type]
    duration: int
    days_of_week: DaysOfWeek
    repeats_every: RepeatsEvery
    progress: float


class Goal(_GoalBase):
    id: Indexed(str, unique=True)  # type: ignore


class GoalCreate(_GoalBase):
    user_id: ObjectIdStr


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

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

    class Settings:
        name = "users"
