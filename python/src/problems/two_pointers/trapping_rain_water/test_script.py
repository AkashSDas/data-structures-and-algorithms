import pytest

from src.problems.two_pointers.trapping_rain_water.script import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),  # Standard case
        ([4, 2, 0, 3, 2, 5], 9),  # Uneven peaks and valleys
        ([2, 0, 2], 2),  # Simple valley
        ([3, 0, 0, 2, 0, 4], 10),  # Multiple valleys
        ([0, 1, 2, 3], 0),  # Increasing slope (no trapped water)
        ([3, 2, 1, 0], 0),  # Decreasing slope (no trapped water)
        ([3], 0),  # Single bar (no trapped water)
        ([], 0),  # Empty list (edge case)
    ],
)
def test_trap(height, expected):
    solution = Solution()
    assert solution.trap(height) == expected
