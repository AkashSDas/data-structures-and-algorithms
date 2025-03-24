import pytest

from src.problems.arrays_and_hashing.valid_anagram.script import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("listen", "silent", True),
        ("heart", "earth", True),
        ("listen", "silence", False),
        ("heart", "earthly", False),
        ("anagram", "anagrams", False),
        ("listen", "list", False),
        ("heart", "hearts", False),
    ],
)
def test_is_anagram(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
