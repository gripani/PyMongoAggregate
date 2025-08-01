from random import randint

from pytest import fixture


@fixture
def a() -> int:
    return randint(0, 10)


@fixture
def b() -> int:
    return randint(0, 10)

@fixture
def code() -> str:
    return "function() {}"
