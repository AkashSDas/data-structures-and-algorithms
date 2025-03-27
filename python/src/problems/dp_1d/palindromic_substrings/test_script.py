import pytest

from src.problems.dp_1d.palindromic_substrings.script import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abc", 3),  # "a", "b", "c"
        ("aaa", 6),  # "a", "a", "a", "aa", "aa", "aaa"
        ("abba", 6),  # "a", "b", "b", "a", "bb", "abba"
        ("racecar", 10),  # All individual letters + "cec", "aceca", "racecar"
        ("a", 1),  # Single character
        ("abcd", 4),  # "a", "b", "c", "d"
        ("aaaa", 10),  # Multiple overlapping palindromes
        ("abccba", 9),  # "a", "b", "c", "c", "b", "a", "cc", "bccb", "abccba"
        ("xyz", 3),  # Only single-character palindromes
        ("aabb", 6),  # "a", "a", "b", "b", "aa", "bb"
    ],
)
def test_count_substrings(s, expected):
    sol = Solution()
    assert sol.countSubstrings(s) == expected
