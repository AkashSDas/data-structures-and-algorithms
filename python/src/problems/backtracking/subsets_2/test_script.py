import pytest

from src.problems.backtracking.subsets_2.script import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    nums = [1, 2, 2]
    expected = sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    result = sorted(solution.subsetsWithDup(nums))
    assert result == expected


def test_example2(solution):
    nums = [0]
    expected = sorted([[], [0]])
    result = sorted(solution.subsetsWithDup(nums))
    assert result == expected


def test_all_duplicates(solution):
    nums = [2, 2, 2]
    expected = sorted([[], [2], [2, 2], [2, 2, 2]])
    result = sorted(solution.subsetsWithDup(nums))
    assert result == expected


def test_no_duplicates(solution):
    nums = [1, 2, 3]
    expected = sorted([[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
    result = sorted(solution.subsetsWithDup(nums))
    assert result == expected


def test_large_numbers(solution):
    nums = [-10, -10, 10]
    expected = sorted([[], [-10], [-10, -10], [-10, -10, 10], [-10, 10], [10]])
    result = sorted(solution.subsetsWithDup(nums))
    assert result == expected
