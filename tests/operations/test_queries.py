from pymongo_aggregate.operations.queries.equals import Equals
from pymongo_aggregate.operations.queries.exists import Exists
from pymongo_aggregate.operations.queries.gt import Gt
from pymongo_aggregate.operations.queries.lt import Lt
from pymongo_aggregate.operations.queries.or_op import Or


def test_equals(a: int):
    op = Equals(a)
    assert op["$eq"] == a


def test_exists():
    op = Exists()
    assert op["$exists"] == 1


def test_or(a: int, b: int):
    op = Or([{"a": a}, {"b": b}])
    assert op["$or"][0]["a"] == a
    assert op["$or"][1]["b"] == b


def test_gt(a: int):
    op = Gt(a)
    assert op["$gt"] == a


def test_lt(a: int):
    op = Lt(a)
    assert op["$lt"] == a
