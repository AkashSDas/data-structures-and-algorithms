import pytest

from src.problems.sliding_window.longest_repeating_character_replacement.script import (
    Solution,
)


@pytest.mark.parametrize(
    "s, k, expected_length",
    [
        ("ABAB", 2, 4),  # Replace two A's or two B's
        ("AABABBA", 1, 4),  # Replace middle A to get "AABBBBA"
        ("AAAA", 2, 4),  # No need to replace, already same letters
        ("ABCDE", 1, 2),  # Replace one character, get 2-length substring
        ("ABCDE", 4, 5),  # Replace all but one, get full string
        ("A", 0, 1),  # Single letter
        ("", 5, 0),  # Empty string
        ("AABBB", 0, 3),  # No operations allowed, longest 'BBB'
        ("BAAAB", 2, 5),  # Replace outer Bs to A's, whole string same
    ],
)
def test_character_replacement(s, k, expected_length):
    sol = Solution()
    assert sol.characterReplacement(s, k) == expected_length
