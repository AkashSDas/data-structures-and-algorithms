import pytest

from src.problems.greedy.partition_labels.script import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),  # Example 1
        ("eccbbbbdec", [10]),  # Example 2
        ("a", [1]),  # Single character case
        ("abac", [3, 1]),  # Two separate partitions
        ("abcde", [1, 1, 1, 1, 1]),  # Every character appears once
        ("aaaaa", [5]),  # All characters are the same
        ("abcdabc", [7]),  # Last occurrence is at the end
        ("abccaddbeffe", [8, 4]),  # Complex case with overlaps
    ],
)
def test_partition_labels(s, expected):
    sol = Solution()
    assert sol.partitionLabels(s) == expected
