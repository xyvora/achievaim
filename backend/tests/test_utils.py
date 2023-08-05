import pytest
from bson.errors import InvalidId

from app.core.utils import process_openai_to_smart_goal, str_to_oid
from app.models.openai import GoalSuggestion
from app.models.smart_goal import GoalInfo, GoalSuggestionCreate


def test_str_to_oid_bad_id():
    with pytest.raises(InvalidId):
        str_to_oid("bad")


def test_process_openai_to_smart_goal():
    data = GoalSuggestion(
        **{
            "id": "chatcmpl-7jtztRhmxfj32OGB6SD1O5scgcAJj",
            "object": "chat.completion",
            "created": 1691174369,
            "model": "gpt-3.5-turbo-0613",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "SMART Goal: Exercise\nSpecific: 30 minutes of exercise, focusing on cardio and strength training, 5 days a week.\nMeasurable: Keep a workout log to track the number of days and duration of exercise each week.\nAchievable: Start with shorter workout sessions and gradually increase duration and intensity as fitness improves. Incorporate activities that are enjoyable and suit individual abilities.\nRelevant: Improve overall fitness, increase strength and endurance, and maintain a healthy lifestyle.\nTime-bound: Maintain the exercise routine for at least 3 months, with continuous progress and improvement.",
                    },
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 174, "completion_tokens": 113, "total_tokens": 287},
        }
    )

    create_goal_info = GoalSuggestionCreate(goal="Exercise")
    result = process_openai_to_smart_goal(data, create_goal_info)

    assert result.model_dump() == {
        "goal": "Exercise",
        "specific": "30 minutes of exercise, focusing on cardio and strength training, 5 days a week.",
        "measurable": "Keep a workout log to track the number of days and duration of exercise each week.",
        "achievable": "Start with shorter workout sessions and gradually increase duration and intensity as fitness improves. Incorporate activities that are enjoyable and suit individual abilities.",
        "relevant": "Improve overall fitness, increase strength and endurance, and maintain a healthy lifestyle.",
        "time_bound": "Maintain the exercise routine for at least 3 months, with continuous progress and improvement.",
    }


def test_process_openai_to_smart_goal_locked():
    data = GoalSuggestion(
        **{
            "id": "chatcmpl-7jtztRhmxfj32OGB6SD1O5scgcAJj",
            "object": "chat.completion",
            "created": 1691174369,
            "model": "gpt-3.5-turbo-0613",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "SMART Goal: Exercise\nSpecific: 30 minutes of exercise, focusing on cardio and strength training, 5 days a week.\nMeasurable: Keep a workout log to track the number of days and duration of exercise each week.\nAchievable: Start with shorter workout sessions and gradually increase duration and intensity as fitness improves. Incorporate activities that are enjoyable and suit individual abilities.\nRelevant: Improve overall fitness, increase strength and endurance, and maintain a healthy lifestyle.\nTime-bound: Maintain the exercise routine for at least 3 months, with continuous progress and improvement.",
                    },
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 174, "completion_tokens": 113, "total_tokens": 287},
        }
    )

    create_goal_info = GoalSuggestionCreate(
        goal="Exercise",
        specific=GoalInfo(info="specific", locked=True),
        measurable=GoalInfo(info="measurable", locked=True),
        achievable=GoalInfo(info="achievable", locked=True),
        relevant=GoalInfo(info="relevant", locked=True),
        time_bound=GoalInfo(info="time bound", locked=True),
    )
    result = process_openai_to_smart_goal(data, create_goal_info)

    assert result.model_dump() == {
        "goal": "Exercise",
        "specific": "specific",
        "measurable": "measurable",
        "achievable": "achievable",
        "relevant": "relevant",
        "time_bound": "time bound",
    }
