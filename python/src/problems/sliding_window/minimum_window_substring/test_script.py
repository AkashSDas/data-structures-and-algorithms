import pytest

from src.problems.sliding_window.minimum_window_substring.script import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),  # Example 1
        ("a", "a", "a"),  # Example 2
        ("a", "aa", ""),  # Example 3
        ("aa", "aa", "aa"),  # Full match with duplicates
        ("ab", "b", "b"),  # Single char match
        ("bba", "ab", "ba"),  # Correct window in middle/end
        ("abdecfab", "abc", "cfab"),  # Possible window at end
        ("abc", "d", ""),  # No matching char
        ("ADOBECODEBANC", "XYZ", ""),  # No match at all
        ("abcabdebac", "cda", "cabd"),  # Needs to include all, minimal
        ("aaflslflsldkalskaaa", "aaa", "aaa"),  # Duplicates of same char
    ],
)
def test_min_window(s, t, expected):
    sol = Solution()
    assert sol.minWindow(s, t) == expected
