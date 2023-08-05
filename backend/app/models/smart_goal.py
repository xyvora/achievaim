from pydantic import BaseModel


class GoalInfo(BaseModel):
    info: str
    locked: bool = False


class GoalSuggestionCreate(BaseModel):
    goal: str
    model: str | None = None
    temperature: float | None = None
    specific: GoalInfo | None = None
    measurable: GoalInfo | None = None
    achievable: GoalInfo | None = None
    relevant: GoalInfo | None = None
    time_bound: GoalInfo | None = None


class SmartGoal(BaseModel):
    goal: str
    specific: str
    measurable: str
    achievable: str
    relevant: str
    time_bound: str
