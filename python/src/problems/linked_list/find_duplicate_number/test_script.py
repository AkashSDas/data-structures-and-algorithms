import pytest

from src.problems.linked_list.find_duplicate_number.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),
        ([2, 2, 2, 2, 2], 2),
        ([1, 1], 1),
        ([1, 2, 4, 3, 5, 6, 7, 4], 4),
    ],
)
def test_find_duplicate(nums, expected):
    s = Solution()
    assert s.findDuplicate(nums) == expected
