import pytest

from src.problems.arrays_and_hashing.group_anagrams.script import Solution

instance = Solution()


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # General case with multiple anagram groups
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        # All words are anagrams of each other
        (
            ["listen", "silent", "inlets", "tinsel"],
            [["listen", "silent", "inlets", "tinsel"]],
        ),
        # No anagrams, all unique words
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
        # Empty input should return an empty list
        ([], []),
        # No anagrams, each word is in its own group
        (["hello", "world", "foo", "bar"], [["hello"], ["world"], ["foo"], ["bar"]]),
    ],
)
def test_group_anagrams(input_data, expected_output):
    result = instance.groupAnagrams(input_data)

    # Convert output and expected to sets of frozensets to handle order-independent comparison
    assert {frozenset(group) for group in result} == {
        frozenset(group) for group in expected_output
    }
