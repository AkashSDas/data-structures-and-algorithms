import pytest

from src.problems.backtracking.subsets.script import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def sort_and_convert(subsets):
    """Helper function to sort subsets and elements inside for comparison."""
    return sorted([sorted(subset) for subset in subsets])


def test_example1(solution):
    nums = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    output = solution.subsets(nums)
    assert sort_and_convert(output) == sort_and_convert(expected)


def test_example2(solution):
    nums = [0]
    expected = [[], [0]]
    output = solution.subsets(nums)
    assert sort_and_convert(output) == sort_and_convert(expected)


def test_empty_input(solution):
    nums = []
    expected = [[]]
    output = solution.subsets(nums)
    assert sort_and_convert(output) == sort_and_convert(expected)


def test_two_elements(solution):
    nums = [4, 5]
    expected = [[], [4], [5], [4, 5]]
    output = solution.subsets(nums)
    assert sort_and_convert(output) == sort_and_convert(expected)


def test_negative_numbers(solution):
    nums = [-1, 0, 1]
    expected = [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]
    output = solution.subsets(nums)
    assert sort_and_convert(output) == sort_and_convert(expected)


def test_max_elements(solution):
    nums = list(range(1, 5))  # 4 elements => 16 subsets
    output = solution.subsets(nums)
    assert len(output) == 16
    # Check uniqueness
    assert len(output) == len(set(tuple(sorted(sub)) for sub in output))


if __name__ == "__main__":
    pytest.main()
