import pytest
from app import add, is_even


def test_add_simple():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_add_zero():
    assert add(5, 0) == 5


@pytest.mark.parametrize("value, expected", [
    (2, True),
    (3, False),
    (10, True),
])
def test_is_even(value, expected):
    assert is_even(value) == expected

@pytest.fixture
def sample_numbers():
    return [2, 4, 6]


def test_all_even(sample_numbers):
    for n in sample_numbers:
        assert is_even(n)