from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str
    content: str


class Choice(BaseModel):
    index: int
    message: Message


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class GoalSuggestion(BaseModel):
    id: str
    obj: str = Field(..., alias="object")
    created: int
    model: str
    choices: list[Choice]
    usage: Usage
