import pytest

from src.problems.backtracking.combination_sum.script import Solution


@pytest.fixture
def solution():
    return Solution()


def sort_combinations(combos):
    """Helper function to sort combinations for consistent comparison."""
    return sorted([sorted(combo) for combo in combos])


def test_example1(solution):
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    output = solution.combinationSum(candidates, target)
    assert sort_combinations(output) == sort_combinations(expected)


def test_example2(solution):
    candidates = [2, 3, 5]
    target = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    output = solution.combinationSum(candidates, target)
    assert sort_combinations(output) == sort_combinations(expected)


def test_example3(solution):
    candidates = [2]
    target = 1
    expected = []
    output = solution.combinationSum(candidates, target)
    assert sort_combinations(output) == sort_combinations(expected)


def test_single_element_match(solution):
    candidates = [7]
    target = 7
    expected = [[7]]
    output = solution.combinationSum(candidates, target)
    assert sort_combinations(output) == sort_combinations(expected)


def test_single_element_no_match(solution):
    candidates = [3]
    target = 2
    expected = []
    output = solution.combinationSum(candidates, target)
    assert sort_combinations(output) == sort_combinations(expected)


def test_large_target(solution):
    candidates = [2, 4]
    target = 10
    expected = [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 4, 4]]
    output = solution.combinationSum(candidates, target)
    assert sort_combinations(output) == sort_combinations(expected)


def test_multiple_candidates(solution):
    candidates = [1, 2]
    target = 4
    expected = [[1, 1, 1, 1], [1, 1, 2], [2, 2]]
    output = solution.combinationSum(candidates, target)
    assert sort_combinations(output) == sort_combinations(expected)


if __name__ == "__main__":
    pytest.main()
