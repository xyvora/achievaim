from typing import Any

from bson import ObjectId


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls) -> Any:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        try:
            return ObjectId(str(v))
        except Exception:
            raise ValueError("Not a valid ObjectId")
