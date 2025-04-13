import pytest

from src.problems.dp_2d.edit_distance.script import Solution


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("horse", "ros", 3),  # Example 1
        ("intention", "execution", 5),  # Example 2
        ("", "", 0),  # Both empty
        ("a", "", 1),  # One character delete
        ("", "a", 1),  # One character insert
        ("abc", "abc", 0),  # No changes needed
        ("abc", "def", 3),  # Replace all
        ("abcdef", "azced", 3),  # Classic test case
        ("kitten", "sitting", 3),  # Replace, replace, insert
        ("flaw", "lawn", 2),  # Delete and insert
    ],
)
def test_min_distance(sol, word1, word2, expected):
    assert sol.minDistance(word1, word2) == expected
