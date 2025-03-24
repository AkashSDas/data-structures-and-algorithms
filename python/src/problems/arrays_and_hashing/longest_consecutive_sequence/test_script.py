import pytest

from src.problems.arrays_and_hashing.longest_consecutive_sequence.script import Solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 1, 2, 3, 4, 5], 6),
        ([1, 2, 3, 4, 5, 6], 6),
        ([9, 8, 7, 6, 5, 4], 6),
        ([1], 1),
        ([], 0),
    ],
)
def test_longest_consecutive(input_data, expected_output):
    solution = Solution()
    assert solution.longestConsecutive(input_data) == expected_output
