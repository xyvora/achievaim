import pytest

from app.models.object_id import ObjectIdStr


def test_invalid_object_id():
    with pytest.raises(ValueError) as exc:
        ObjectIdStr.validate("bad")

    assert "Not a valid ObjectId" in str(exc.value)
