import pytest

from src.problems.greedy.merge_triplets_to_form_target_triplet.script import Solution


@pytest.mark.parametrize(
    "triplets, target, expected",
    [
        # Example cases
        ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),
        ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),
        ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True),
        # Edge Cases
        ([[1, 1, 1]], [1, 1, 1], True),  # Single triplet matches target
        ([[1, 2, 3], [2, 3, 4], [3, 4, 5]], [4, 5, 6], False),  # Cannot reach target
        ([[5, 5, 5]], [5, 5, 5], True),  # Target already exists in triplets
        ([[1, 1, 2], [1, 2, 1], [2, 1, 1]], [2, 2, 2], True),
        # Large Input Case
        (
            [[i, i, i] for i in range(1, 1001)],
            [1000, 1000, 1000],
            True,
        ),  # Largest possible case
    ],
)
def test_mergeTriplets(triplets, target, expected):
    solution = Solution()
    assert solution.mergeTriplets(triplets, target) == expected
