import pytest

from src.problems.backtracking.combination_sum_2.script import Solution


@pytest.fixture
def solution():
    return Solution()


def sort_result(combos):
    """Sort combinations and internal lists for easier comparison."""
    return sorted([sorted(combo) for combo in combos])


def test_example1(solution):
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


def test_example2(solution):
    candidates = [2, 5, 2, 1, 2]
    target = 5
    expected = [[1, 2, 2], [5]]
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


def test_no_combination(solution):
    candidates = [4, 5, 6]
    target = 3
    expected = []
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


def test_single_element_match(solution):
    candidates = [3]
    target = 3
    expected = [[3]]
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


def test_single_element_no_match(solution):
    candidates = [4]
    target = 3
    expected = []
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


def test_large_duplicates(solution):
    candidates = [1, 1, 1, 1, 2, 2]
    target = 4
    expected = [[1, 1, 2], [2, 2], [1, 1, 1, 1]]
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


def test_all_elements_sum_to_target(solution):
    candidates = [1, 2, 3]
    target = 6
    expected = [[1, 2, 3]]
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


def test_empty_candidates(solution):
    candidates = []
    target = 5
    expected = []
    output = solution.combinationSum2(candidates, target)
    assert sort_result(output) == sort_result(expected)


if __name__ == "__main__":
    pytest.main()
