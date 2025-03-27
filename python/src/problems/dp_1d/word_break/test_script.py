import pytest

from src.problems.dp_1d.word_break.script import Solution


@pytest.mark.parametrize(
    "s, wordDict, expected",
    [
        ("leetcode", ["leet", "code"], True),  # "leetcode" -> "leet code"
        (
            "applepenapple",
            ["apple", "pen"],
            True,
        ),  # "applepenapple" -> "apple pen apple"
        (
            "catsandog",
            ["cats", "dog", "sand", "and", "cat"],
            False,
        ),  # No valid segmentation
        ("a", ["a"], True),  # Single character in dictionary
        ("b", ["a"], False),  # Single character not in dictionary
        ("cars", ["car", "ca", "rs"], True),  # "cars" -> "car s" or "ca rs"
        ("aaaaaaa", ["aaaa", "aaa"], True),  # "aaaaaaa" -> "aaaa aaa"
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            True,
        ),  # "pine apple pen apple"
        ("abcd", ["a", "abc", "b", "cd"], True),  # "abcd" -> "abc d" or "a b cd"
        ("abcd", ["ab", "abc", "cd"], True),  # "abcd" -> "ab cd"
        ("dogcatsdog", ["dog", "cats", "dogcat"], True),  # "dog cats dog"
    ],
)
def test_word_break(s, wordDict, expected):
    sol = Solution()
    assert sol.wordBreak(s, wordDict) == expected
