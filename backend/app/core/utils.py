from collections.abc import Callable
from typing import Any

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter as FastAPIRouter
from fastapi.types import DecoratedCallable

from app.api.deps import logger
from app.models.openai import GoalSuggestion
from app.models.smart_goal import SmartGoal


class APIRouter(FastAPIRouter):
    def api_route(
        self, path: str, *, include_in_schema: bool = True, **kwargs: Any
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        """Updated api_route function that automatically configures routes to have 2 versions.

        One without a trailing slash and another with it.
        """
        if path.endswith("/"):
            path = path[:-1]

        add_path = super().api_route(path, include_in_schema=include_in_schema, **kwargs)

        alternate_path = f"{path}/"
        add_alternate_path = super().api_route(alternate_path, include_in_schema=False, **kwargs)

        def decorator(func: DecoratedCallable) -> DecoratedCallable:
            add_alternate_path(func)
            return add_path(func)

        return decorator


def process_openai_to_smart_goal(goal: GoalSuggestion) -> SmartGoal:
    goal_info = goal.choices[0].message.content.split("\n")
    smart_goal: dict[str, str] = {}
    for info in goal_info:
        info_parts = info.split(": ", maxsplit=1)

        match info_parts[0]:
            case "SMART Goal":
                smart_goal["goal"] = info_parts[1]
            case "Specific":
                smart_goal["specific"] = info_parts[1]
            case "Measurable":
                smart_goal["measurable"] = info_parts[1]
            case "Achievable":
                smart_goal["achievable"] = info_parts[1]
            case "Relevant":
                smart_goal["relevant"] = info_parts[1]
            case "Time-bound":
                smart_goal["time_bound"] = info_parts[1]

    return SmartGoal(**smart_goal)


def str_to_oid(id_str: str) -> ObjectId:
    try:
        return ObjectId(id_str)
    except InvalidId:
        logger.info(f"{id_str} is not a valid ObjectId")
        raise
