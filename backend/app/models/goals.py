from enum import Enum

from beanie import Document, Indexed
from camel_converter import to_camel
from camel_converter.pydantic_base import CamelBase


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


class GoalBase(CamelBase):
    name: str
    duration: int
    days_of_week: DaysOfWeek
    repeats_every: RepeatsEvery
    progress: float


class GoalUpdate(GoalBase):
    id: str
    name: str
    duration: int
    days_of_week: DaysOfWeek
    repeats_every: RepeatsEvery
    progress: float


class Goal(Document):
    name: Indexed(str, unique=True)  # type: ignore[valid-type]
    duration: int
    days_of_week: DaysOfWeek
    repeats_every: RepeatsEvery
    progress: float

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
