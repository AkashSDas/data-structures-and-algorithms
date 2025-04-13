import pytest

from src.problems.maths.happy_number.script import Solution


@pytest.fixture
def solver():
    return Solution()


def test_example_true(solver):
    assert solver.isHappy(19) is True


def test_example_false(solver):
    assert solver.isHappy(2) is False


def test_single_digit_true(solver):
    assert solver.isHappy(1) is True


def test_single_digit_false(solver):
    assert solver.isHappy(4) is False


def test_large_happy_number(solver):
    assert solver.isHappy(100) is True


def test_large_unhappy_number(solver):
    assert solver.isHappy(116) is False


def test_edge_case_7(solver):
    # 7 is a known happy number
    assert solver.isHappy(7) is True


def test_edge_case_20(solver):
    assert solver.isHappy(20) is False
