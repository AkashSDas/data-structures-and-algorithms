import pytest

from src.problems.greedy.jump_game_2.script import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),  # Example 1
        ([2, 3, 0, 1, 4], 2),  # Example 2
        ([1, 1, 1, 1], 3),  # Minimum jumps every step
        ([6, 2, 4, 0, 5, 1, 1, 4, 2, 9], 2),  # A large jump at start
        ([1, 2, 1, 1, 1], 3),  # Different small jumps
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 2),  # Large jumps
        ([1] * 1000, 999),  # Worst case with smallest jumps
        ([1000] + [1] * 999, 1),  # Single jump from start to end
    ],
)
def test_jump(nums, expected):
    sol = Solution()
    assert sol.jump(nums) == expected
