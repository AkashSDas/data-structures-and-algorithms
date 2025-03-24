import pytest

from src.problems.heap_priority_queue.kth_largest_element_in_an_array.script import (
    Solution,
)


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    expected = 5
    result = solution.findKthLargest(nums, k)
    assert result == expected


def test_example2(solution):
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    expected = 4
    result = solution.findKthLargest(nums, k)
    assert result == expected


def test_single_element(solution):
    nums = [1]
    k = 1
    expected = 1
    result = solution.findKthLargest(nums, k)
    assert result == expected


def test_all_same_elements(solution):
    nums = [2, 2, 2, 2, 2]
    k = 3
    expected = 2
    result = solution.findKthLargest(nums, k)
    assert result == expected


def test_k_equals_length(solution):
    nums = [7, 6, 5, 4, 3, 2, 1]
    k = 7
    expected = 1
    result = solution.findKthLargest(nums, k)
    assert result == expected


def test_large_numbers(solution):
    nums = [1000, 2000, 3000, 4000, 5000]
    k = 3
    expected = 3000
    result = solution.findKthLargest(nums, k)
    assert result == expected


def test_negative_numbers(solution):
    nums = [-10, -20, -30, -40, -50]
    k = 2
    expected = -20
    result = solution.findKthLargest(nums, k)
    assert result == expected


def test_unsorted_and_duplicates(solution):
    nums = [5, 3, 1, 6, 4, 6, 2, 6, 3]
    k = 2
    expected = 6
    result = solution.findKthLargest(nums, k)
    assert result == expected
