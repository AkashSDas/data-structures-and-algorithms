import pytest

from src.problems.dp_1d.longest_palindromic_substring.script import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("babad", "bab"),  # "aba" is also valid
        ("cbbd", "bb"),  # The longest palindrome is "bb"
        ("a", "a"),  # Single character is a palindrome itself
        ("ac", "a"),  # Either "a" or "c" can be the answer
        ("racecar", "racecar"),  # Entire string is a palindrome
        ("abccba", "abccba"),  # Entire string is the longest palindrome
        ("abcdef", "a"),  # Any single character can be the answer
        ("aaaabaaa", "aaabaaa"),  # Longest palindrome is in the middle
        ("abaxyzzyxf", "xyzzyx"),  # Palindrome in the middle
        ("", ""),  # Empty string case
        ("abba", "abba"),  # Even-length palindrome
        ("a" * 1000, "a" * 1000),  # Large input, all same characters
    ],
)
def test_longest_palindrome(s, expected):
    sol = Solution()
    result = sol.longestPalindrome(s)
    assert (
        result == expected or result[::-1] == expected
    )  # Accept reversed valid answers
