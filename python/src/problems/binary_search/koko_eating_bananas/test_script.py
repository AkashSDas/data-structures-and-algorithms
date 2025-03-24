import pytest

from src.problems.binary_search.koko_eating_bananas.script import Solution


@pytest.mark.parametrize(
    "piles, h, expected",
    [
        ([3, 6, 7, 11], 8, 4),  # Example 1
        ([30, 11, 23, 4, 20], 5, 30),  # Example 2
        ([30, 11, 23, 4, 20], 6, 23),  # Example 3
        ([1000000000], 2, 500000000),  # Large pile, split over hours
        ([1, 1, 1, 1, 1], 5, 1),  # Already minimal eating speed
        ([1, 1, 1, 1, 1], 10, 1),  # More hours than piles, always eat 1 per hour
        ([805306368, 805306368, 805306368], 3, 805306368),  # Large numbers edge case
        ([5, 10, 20], 6, 7),  # Exact split into hours
        ([10, 20, 30, 40], 4, 40),  # One pile per hour
        ([30, 11, 23, 4, 20], 7, 20),  # Can slow down a bit more
    ],
)
def test_min_eating_speed(piles, h, expected):
    solution = Solution()
    assert solution.minEatingSpeed(piles, h) == expected
