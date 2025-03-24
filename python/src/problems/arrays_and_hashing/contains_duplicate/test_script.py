import pytest

from src.problems.arrays_and_hashing.contains_duplicate.script import contains_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),  # Returns true if there are duplicates
        ([1, 2, 3, 4], False),  # Returns false if there are no duplicates
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], True),  # Large array with duplicates
        ([], False),  # Empty array
        ([1], False),  # Single element array
    ],
)
def test_contains_duplicate(nums, expected):
    assert contains_duplicate(nums) == expected
