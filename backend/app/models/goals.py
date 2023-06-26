from datetime import UTC, datetime
from enum import Enum

from beanie import Document, Indexed
from camel_converter import to_camel
from camel_converter.pydantic_base import CamelBase
from pydantic import Field, validator


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


class Goal(Document):
    name: Indexed(str, unique=True)  # type: ignore[valid-type]
    duration: int
    days_of_week: DaysOfWeek
    repeats_every: RepeatsEvery
    progress: float
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @validator("updated_at", pre=True)
    @classmethod
    def set_updated_at(cls, _: datetime) -> datetime:
        return datetime.now(tz=UTC)

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
