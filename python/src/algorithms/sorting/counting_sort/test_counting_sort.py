import pytest

from src.algorithms.sorting.counting_sort.counting_sort import counting_sort


@pytest.mark.parametrize(
    "input_arr, expected",
    [
        ([], []),  # Empty list
        ([0], [0]),  # Single element
        ([2, 1, 0], [0, 1, 2]),  # Three elements unsorted
        ([3, 3, 3], [3, 3, 3]),  # All same elements
        (
            [4, 2, 2, 8, 3, 3, 1],
            [1, 2, 2, 3, 3, 4, 8],
        ),  # Random unsorted list with duplicates
        ([0, 0, 0, 0], [0, 0, 0, 0]),  # All zeros
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),  # Reverse sorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
    ],
)
def test_counting_sort(input_arr, expected):
    counting_sort(input_arr)
    assert input_arr == expected
