import pytest

from src.algorithms.sorting.merge_sort.merge_sort import merge_sort


@pytest.mark.parametrize(
    "input_arr, expected",
    [
        ([], []),  # Empty array
        ([1], [1]),  # Single element
        ([2, 1], [1, 2]),  # Two elements
        ([3, 2, 1], [1, 2, 3]),  # Reverse sorted
        ([1, 2, 3], [1, 2, 3]),  # Already sorted
        ([4, 3, 5, 1, 2], [1, 2, 3, 4, 5]),  # Random unsorted
        ([5, 5, 5, 5], [5, 5, 5, 5]),  # All duplicates
        ([0, -1, 3, -2, 2], [-2, -1, 0, 2, 3]),  # Including negatives
    ],
)
def test_insertion_sort(input_arr, expected):
    merge_sort(input_arr)
    assert input_arr == expected
