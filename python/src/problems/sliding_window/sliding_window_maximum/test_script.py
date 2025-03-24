import pytest

from src.problems.sliding_window.sliding_window_maximum.script import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
        ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 2, [2, 3, 4, 5]),  # Increasing order
        ([5, 4, 3, 2, 1], 2, [5, 4, 3, 2]),  # Decreasing order
        ([7, 2, 4], 2, [7, 4]),  # Random case
    ],
)
def test_max_sliding_window(nums, k, expected):
    sol = Solution()
    assert sol.maxSlidingWindow(nums, k) == expected
