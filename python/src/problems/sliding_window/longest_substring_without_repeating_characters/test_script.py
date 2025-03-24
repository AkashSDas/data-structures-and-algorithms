import pytest

from src.problems.sliding_window.longest_substring_without_repeating_characters.script import (
    Solution,
)


@pytest.mark.parametrize(
    "s, expected_length",
    [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),  # "b"
        ("pwwkew", 3),  # "wke"
        ("", 0),  # empty string
        ("a", 1),  # single character
        ("abcdef", 6),  # all unique
        ("abba", 2),  # "ab" or "ba"
        ("dvdf", 3),  # "vdf"
        ("tmmzuxt", 5),  # "mzuxt"
    ],
)
def test_length_of_longest_substring(s, expected_length):
    sol = Solution()
    assert sol.lengthOfLongestSubstring(s) == expected_length
