import pytest
from bson.errors import InvalidId

from app.core.utils import str_to_oid


def test_str_to_oid_bad_id():
    with pytest.raises(InvalidId):
        str_to_oid("bad")
