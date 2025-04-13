import pytest

from src.problems.dp_2d.interleaving_string.script import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "s1, s2, s3, expected",
    [
        ("aabcc", "dbbca", "aadbbcbcac", True),  # Example 1
        ("aabcc", "dbbca", "aadbbbaccc", False),  # Example 2
        ("", "", "", True),  # Example 3 (all empty)
        ("", "abc", "abc", True),  # s1 empty
        ("abc", "", "abc", True),  # s2 empty
        ("abc", "def", "adbcef", True),  # Interleaving of two disjoint strings
        ("abc", "def", "abcdef", True),  # Straight concatenation
        ("abc", "def", "abdecf", True),
        ("abc", "def", "abcfde", False),  # Wrong interleave
        ("aa", "ab", "aaba", True),  # Repeated characters
        ("a", "b", "ab", True),  # Single character strings
        ("a", "b", "ba", True),  # Swap single chars
        ("a", "b", "aa", False),  # Impossible case
    ],
)
def test_is_interleave(sol, s1, s2, s3, expected):
    assert sol.isInterleave(s1, s2, s3) == expected
