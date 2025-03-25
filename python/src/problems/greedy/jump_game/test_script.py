import pytest

from src.problems.greedy.jump_game.script import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], True),  # Can reach the last index
        ([3, 2, 1, 0, 4], False),  # Stuck at index 3
        ([0], True),  # Single element, already at last index
        ([1, 2, 3, 4, 5], True),  # Increasing jumps, always reachable
        ([5, 4, 3, 2, 1, 0, 0, 0, 4], False),  # Stuck due to zeroes
        ([2, 0, 0], True),  # Jump over zeroes
        ([1, 1, 1, 0], True),  # Can reach last index exactly
        ([1, 1, 0, 1], False),  # Stuck at index 2
    ],
)
def test_can_jump(solution, nums, expected):
    assert solution.canJump(nums) == expected
