from pydantic import BaseModel


class GoalSuggestionCreate(BaseModel):
    goal: str
    model: str | None = None
    temperature: float | None = None


class SmartGoal(BaseModel):
    goal: str
    specific: str
    measurable: str
    achievable: str
    relevant: str
    time_bound: str
