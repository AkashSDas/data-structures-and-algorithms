import pytest

from src.problems.dp_1d.maximum_product_subarray.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, -2, 4], 6),  # [2,3] gives max product 6
        (
            [-2, 0, -1],
            0,
        ),  # The result cannot be 2, because [-2,-1] is not a contiguous subarray
        ([0, 2], 2),  # The max product is 2
        ([3, -1, 4], 4),  # The max product is 4
        ([-2, -3, 7], 42),  # [-2,-3,7] gives max product 42
        ([1, 2, 3, 4], 24),  # Entire array gives max product
        ([1, -2, -3, 4], 24),  # [-2,-3,4] gives max product 12
        ([-1, -2, -3, -4], 24),  # Even negatives result in a positive product
        ([0, -1, -2, -3, -4], 24),  # [-1,-2,-3,-4] gives max product 24
        ([1, 0, -1, 2, 3, -5, -2], 60),  # [2,3,-5,-2] gives max product 60
        ([-1], -1),  # Single negative number
        ([10], 10),  # Single positive number
    ],
)
def test_max_product(nums, expected):
    sol = Solution()
    assert sol.maxProduct(nums) == expected
