import pytest

from src.problems.maths.plus_one.script import Solution


@pytest.fixture
def solver():
    return Solution()


def test_example_1(solver):
    assert solver.plusOne([1, 2, 3]) == [1, 2, 4]


def test_example_2(solver):
    assert solver.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_example_3(solver):
    assert solver.plusOne([9]) == [1, 0]


def test_all_nines(solver):
    assert solver.plusOne([9, 9, 9]) == [1, 0, 0, 0]


def test_with_carry_in_middle(solver):
    assert solver.plusOne([1, 9, 9]) == [2, 0, 0]


def test_single_digit_no_carry(solver):
    assert solver.plusOne([5]) == [6]


def test_trailing_zero(solver):
    assert solver.plusOne([1, 0, 0]) == [1, 0, 1]


def test_large_number(solver):
    assert solver.plusOne([3, 2, 1, 0, 9]) == [3, 2, 1, 1, 0]
