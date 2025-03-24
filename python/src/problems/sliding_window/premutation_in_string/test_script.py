import pytest

from src.problems.sliding_window.premutation_in_string.script import Solution


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ab", "eidbaooo", True),  # s2 contains "ba" which is permutation of "ab"
        ("ab", "eidboaoo", False),  # no permutation present
        ("adc", "dcda", True),  # s2 contains "cda" which is permutation of "adc"
        ("a", "a", True),  # trivial case, both are same
        ("abc", "ccccbbbbaaaa", False),  # letters present but not enough
        ("xyz", "afdgzyxksldfm", True),  # s2 contains "zyx" permutation
        ("hello", "ooolleoooleh", False),  # no permutation
        ("", "anything", True),  # empty s1 is trivially in s2
        ("a", "", False),  # s2 is empty
        ("abcd", "abc", False),  # s2 shorter than s1
    ],
)
def test_check_inclusion(s1, s2, expected):
    sol = Solution()
    assert sol.checkInclusion(s1, s2) == expected
