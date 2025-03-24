import pytest

from src.problems.two_pointers.container_with_most_water.script import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # Standard case
        ([1, 1], 1),  # Smallest valid case
        ([4, 3, 2, 1, 4], 16),  # Taller bars at both ends
        ([1, 2, 1], 2),  # Middle lower than sides
        ([1, 3, 2, 5, 25, 24, 5], 24),  # Large peak at the end
        ([2, 3, 10, 5, 7, 8, 9], 36),  # High peak in middle
        ([1, 2, 4, 3], 4),  # Increasing then decreasing
        ([100, 1, 100], 200),  # Large heights at edges
        ([1], 0),  # Single height (no area)
        ([], 0),  # Empty list (edge case)
    ],
)
def test_maxArea(height, expected):
    solution = Solution()
    assert solution.maxArea(height) == expected
