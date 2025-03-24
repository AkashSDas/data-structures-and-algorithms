import pytest
from typing import List

from src.algorithms.sorting.selection_sort.selection_sort import selection_sort


@pytest.mark.parametrize(
    "input_arr, expected",
    [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
        ([2, 1, 4, 3, 5], [1, 2, 3, 4, 5]),  # Random order
        ([1], [1]),  # Single element
        ([], []),  # Empty list
        ([3, 3, 3], [3, 3, 3]),  # All duplicates
        ([5, 1, 5, 2, 5], [1, 2, 5, 5, 5]),  # Duplicates & unique
        ([0, -1, -3, 2, 1], [-3, -1, 0, 1, 2]),  # Negative numbers
    ],
)
def test_selection_sort(input_arr: List[int], expected: List[int]):
    selection_sort(input_arr)
    assert input_arr == expected
