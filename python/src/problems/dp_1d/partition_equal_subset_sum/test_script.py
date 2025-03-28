import pytest

from src.problems.dp_1d.partition_equal_subset_sum.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 5, 11, 5], True),  # Can be split into [1,5,5] and [11]
        ([1, 2, 3, 5], False),  # Cannot be split into equal sum subsets
        ([2, 2, 3, 5], False),  # Odd sum, impossible
        ([1, 1, 1, 1, 2, 2, 2, 2], True),  # Can be split into two equal parts
        ([3, 3, 3, 4, 5], True),  # Possible split: [3,3,3] and [4,5]
        ([1], False),  # Single element cannot be split
        (
            [
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
            ],
            True,
        ),  # Large input
        ([1, 2, 5], False),  # Cannot split evenly
    ],
)
def test_can_partition(nums, expected):
    sol = Solution()
    assert sol.canPartition(nums) == expected
