from datetime import datetime

from beanie import Document
from bson import ObjectId
from pydantic import AnyHttpUrl, BaseModel, Field, validator
from pymongo import ASCENDING, IndexModel

from app.models.object_id import ObjectIdStr


class DaysOfWeek(BaseModel):
    monday: bool = False
    tuesday: bool = False
    wednesday: bool = False
    thursday: bool = False
    friday: bool = False
    saturday: bool = False
    sunday: bool = False


class _GoalBase(BaseModel):
    goal: str
    specific: str | None = None
    measurable: str | None = None
    attainable: str | None = None
    relevant: str | None = None
    date_for_achievement: datetime | None = None
    days_of_week: DaysOfWeek | None = None
    time_of_day: str | None
    progress: float | None = None

    @validator("time_of_day")
    @classmethod
    def validate_time_of_day(cls, v: str | None) -> str | None:
        if not v:
            return None

        split_time = v.split(":", maxsplit=1)

        if len(split_time) != 2:
            raise ValueError(f"{v} is not a valid time")

        try:
            hour = int(split_time[0])
            minutes = int(split_time[1])
        except ValueError:
            raise ValueError(f"{v} is not a valid time")

        if 0 > hour > 23:
            raise ValueError(f"{v} is not a valid time")

        if 0 > minutes > 59:
            raise ValueError(f"{v} is not a valid time")

        return v


class Goal(_GoalBase):
    id: str

    class Settings:
        projection = {
            "id": "$_id",
            "goal": "$goal",
            "specific": "$specific",
            "measurable": "$measurable",
            "attainable": "$attainable",
            "relevant": "$relevant",
            "date_for_achievement": "$date_for_achievement",
            "days_of_week": "$days_of_week",
            "time_of_day": "$time_of_day",
            "progress": "$prograss",
        }


class GoalCreate(_GoalBase):
    pass


class GoalWithUserId(Goal):
    user_id: ObjectIdStr

    class Config:
        json_encoders = {ObjectId: lambda x: str(x)}


class UserCreate(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    country: str | None = None
    avatar_url: AnyHttpUrl | None = None
    password: str


class UserNoPassword(BaseModel):
    id: ObjectIdStr
    user_name: str
    first_name: str
    last_name: str
    country: str
    avatar_url: AnyHttpUrl | None = None

    class Config:
        json_encoders = {ObjectId: lambda x: str(x)}

    class Settings:
        projection = {
            "id": "$_id",
            "user_name": "$user_name",
            "first_name": "$first_name",
            "last_name": "$last_name",
            "country": "$country",
            "avatar_url": "$avatar_url",
        }


class UserWithGoals(UserNoPassword):
    goals: list[Goal] | None = None

    class Settings:
        projection = {
            "id": "$_id",
            "user_name": "$user_name",
            "first_name": "$first_name",
            "last_name": "$last_name",
            "country": "$country",
            "avatar_url": "$avatar_url",
            "goals": "$goals",
        }


class UserNoGoals(UserNoPassword):
    is_active: bool
    is_admin: bool
    date_created: datetime
    last_update: datetime
    last_login: datetime

    class Settings:
        projection = {
            "id": "$_id",
            "user_name": "$user_name",
            "first_name": "$first_name",
            "last_name": "$last_name",
            "country": "$country",
            "avatar_url": "$avatar_url",
            "is_active": "$is_active",
            "is_admin": "$is_admin",
            "date_created": "$date_created",
            "last_update": "$last_update",
            "last_login": "$last_login",
        }


class UserUpdateMe(BaseModel):
    id: ObjectIdStr
    password: str
    user_name: str
    first_name: str
    last_name: str
    country: str
    avatar_url: AnyHttpUrl | None = None

    class Config:
        json_encoders = {ObjectId: lambda x: str(x)}


class UserUpdate(UserUpdateMe):
    is_active: bool
    is_admin: bool


class User(Document):
    user_name: str
    first_name: str
    last_name: str
    country: str
    hashed_password: str
    avatar_url: AnyHttpUrl | None = None
    goals: list[Goal] | None = None
    is_active: bool = True
    is_admin: bool = False
    date_created: datetime = Field(default_factory=datetime.now)
    last_update: datetime = Field(default_factory=datetime.now)
    last_login: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "users"
        indexes = [
            IndexModel(keys=[("user_name", ASCENDING)], name="user_name", unique=True),
            IndexModel(keys=[("is_active", ASCENDING)], name="is_active"),
            IndexModel(keys=[("is_admin", ASCENDING)], name="is_admin"),
            IndexModel(keys=[("goals", ASCENDING)], name="goals"),
            IndexModel(
                keys=[("_id", ASCENDING), ("goals.id", ASCENDING)], name="goal_id", unique=True
            ),
            IndexModel(
                keys=[("_id", ASCENDING), ("goals.goal", ASCENDING)], name="goal", unique=True
            ),
        ]

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

        goals = {x.goal for x in v}
        if len(v) != len(goals):
            raise ValueError(
                "Goal names must be unique",
            )

        return v
