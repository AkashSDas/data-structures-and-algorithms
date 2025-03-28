import pytest

from src.problems.dp_1d.longest_increasing_subsequence.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # LIS: [2,3,7,101]
        ([0, 1, 0, 3, 2, 3], 4),  # LIS: [0,1,2,3]
        ([7, 7, 7, 7, 7, 7, 7], 1),  # LIS: [7]
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            10,
        ),  # LIS: Entire array (strictly increasing)
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1),  # LIS: Any single element
        ([3, 10, 2, 1, 20], 3),  # LIS: [3,10,20]
        ([50, 3, 10, 7, 40, 80], 4),  # LIS: [3, 7, 40, 80]
        ([1], 1),  # Single element
        ([4, 10, 4, 3, 8, 9], 3),  # LIS: [4, 8, 9]
        ([2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2], 2),  # LIS: [2,3]
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),  # LIS: [1,3,4,5,6,10]
    ],
)
def test_length_of_lis(nums, expected):
    sol = Solution()
    assert sol.lengthOfLIS(nums) == expected
