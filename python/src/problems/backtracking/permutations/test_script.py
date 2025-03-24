import pytest

from src.problems.backtracking.permutations.script import Solution


@pytest.fixture
def solution():
    return Solution()


def sort_permutations(perms):
    """Sort permutations and internal lists for comparison."""
    return sorted([list(p) for p in perms])


def test_example1(solution):
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    output = solution.permute(nums)
    assert sort_permutations(output) == sort_permutations(expected)


def test_example2(solution):
    nums = [0, 1]
    expected = [[0, 1], [1, 0]]
    output = solution.permute(nums)
    assert sort_permutations(output) == sort_permutations(expected)


def test_example3(solution):
    nums = [1]
    expected = [[1]]
    output = solution.permute(nums)
    assert sort_permutations(output) == sort_permutations(expected)


def test_negative_numbers(solution):
    nums = [-1, 2]
    expected = [[-1, 2], [2, -1]]
    output = solution.permute(nums)
    assert sort_permutations(output) == sort_permutations(expected)


def test_three_elements_with_zero(solution):
    nums = [0, -1, 1]
    expected = [[0, -1, 1], [0, 1, -1], [-1, 0, 1], [-1, 1, 0], [1, 0, -1], [1, -1, 0]]
    output = solution.permute(nums)
    assert sort_permutations(output) == sort_permutations(expected)


def test_larger_input(solution):
    nums = [1, 2, 3, 4]
    output = solution.permute(nums)
    assert len(output) == 24  # 4! = 24 permutations
    # Ensure all permutations are unique
    assert len(output) == len(set(tuple(p) for p in output))


if __name__ == "__main__":
    pytest.main()
