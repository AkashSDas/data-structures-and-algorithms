import pytest

from src.problems.heap_priority_queue.last_stone_weight.script import Solution


@pytest.fixture
def solver():
    return Solution()


def test_example_1(solver):
    assert solver.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1


def test_example_2(solver):
    assert solver.lastStoneWeight([1]) == 1


def test_empty_stones(solver):
    assert solver.lastStoneWeight([]) == 0


def test_all_equal_stones(solver):
    assert solver.lastStoneWeight([3, 3, 3, 3]) == 0


def test_large_numbers(solver):
    assert solver.lastStoneWeight([1000, 2000, 3000, 4000]) == 0


def test_two_stones_equal(solver):
    assert solver.lastStoneWeight([5, 5]) == 0


def test_two_stones_different(solver):
    assert solver.lastStoneWeight([7, 4]) == 3


def test_single_large_stone(solver):
    assert solver.lastStoneWeight([99999]) == 99999


def test_multiple_zero_result(solver):
    assert solver.lastStoneWeight([10, 4, 6]) == 0


def test_multiple_one_result(solver):
    assert solver.lastStoneWeight([9, 3, 2, 2, 1]) == 1
