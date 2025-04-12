import pytest

from src.problems.dp_2d.longest_common_sequence.script import Solution


@pytest.mark.parametrize(
    "text1, text2, expected",
    [
        ("abcde", "ace", 3),  # common subsequence: "ace"
        ("abc", "abc", 3),  # identical strings
        ("abc", "def", 0),  # no common characters
        ("", "", 0),  # both strings empty
        ("a", "a", 1),  # one common char
        ("abc", "", 0),  # one empty string
        ("", "abc", 0),  # one empty string
        ("bsbininm", "jmjkbkjkv", 1),  # minimal match
        ("abcdefg", "xyzabc", 3),  # common subsequence: "abc"
        ("a" * 1000, "a" * 1000, 1000),  # max size identical
    ],
)
def test_longest_common_subsequence(text1, text2, expected):
    sol = Solution()
    assert sol.longestCommonSubsequence(text1, text2) == expected
