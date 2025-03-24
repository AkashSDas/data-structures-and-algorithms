import pytest
from src.algorithms.sorting.bubble_sort.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "input_arr, expected",
    [
        ([], []),  # Empty list
        ([1], [1]),  # Single element
        ([2, 1], [1, 2]),  # Two elements unsorted
        ([1, 2], [1, 2]),  # Two elements sorted
        ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),  # Random unsorted list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted
        ([3, 3, 3], [3, 3, 3]),  # All elements same
        ([9, 7, 5, 3, 3, 2, 1], [1, 2, 3, 3, 5, 7, 9]),  # Duplicate values
    ],
)
def test_bubble_sort(input_arr, expected):
    bubble_sort(input_arr)
    assert input_arr == expected
