from httpx import AsyncClient

from app.core.config import config
from app.exceptions import (
    InvalidApiKeyError,
    InvalidTemperatureError,
    OpenAiError,
    QuotaExceededError,
)
from app.models.openai import GoalSuggestion


async def generate_smart_goal(
    goal: str, *, model: str | None = None, temperature: float | None = None
) -> GoalSuggestion:
    prompt = f"""SMART Goal: {goal}
Specific:
Measureable:
Achievable:
Relevant:
Time-bound:

You are a SMART Goal Coach using the SMART method: Specific, Measurable, Achievable, Relevant, Time-bound. Here's what each part means:

Specific: Clear, detailed goal.
Measurable: Criteria to track progress.
Achievable: Realistic and within reach.
Relevant: Aligns with other goals.
Time-bound: Deadline or time frame.
I will share my SMART Goal (e.g., "Daily Exercise"), and you will help me detail it.

Example:
SMART Goal: Exercise
Specific: 15 min daily exercise.
Measurable: Track consecutive days.
Achievable: Find enjoyable activities.
Relevant: Improve fitness.
Time-bound: 30 consecutive days.

If any details are missing, infer the best suggestion.
"""
    if temperature:
        if 0 > temperature or temperature > 2:
            raise InvalidTemperatureError("temperature must be between 0 and 2")
    else:
        temperature = 1

    if not model:
        model = "gpt-3.5-turbo"

    headers = {
        "Content-Type": "application/json",
        "authorization": f"Bearer {config.openai_api_key}",
    }

    if config.openai_organization:
        headers["OpenAI-Organization"] = config.openai_organization

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }

    # OpenAI responses are SLOW so I increased the timeout.
    async with AsyncClient(timeout=30) as client:
        response = await client.post(config.openai_url, headers=headers, json=data)

        if response.status_code == 401:
            raise InvalidApiKeyError("Incorrect API key provided")

        if response.status_code == 429:
            raise QuotaExceededError("OpenAI quota exceeded")

        if response.status_code != 200:
            raise OpenAiError(
                f"An error occurred with the OpenAI request: status code: {response.status_code}, detail: {response.json()}"
            )

        return GoalSuggestion(**response.json())
