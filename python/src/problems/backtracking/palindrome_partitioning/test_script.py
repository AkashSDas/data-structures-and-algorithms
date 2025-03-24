import pytest
from collections import Counter

from src.problems.backtracking.palindrome_partitioning.script import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example_1(sol):
    s = "aab"
    result = sol.partition(s)
    expected = [["a", "a", "b"], ["aa", "b"]]
    # Sort inner lists and outer list to compare regardless of order
    assert sorted([sorted(sublist) for sublist in result]) == sorted(
        [sorted(sublist) for sublist in expected]
    )


def test_example_2(sol):
    s = "a"
    result = sol.partition(s)
    expected = [["a"]]
    assert result == expected


def test_all_same_characters(sol):
    s = "aaa"
    result = sol.partition(s)
    expected = [["a", "a", "a"], ["aa", "a"], ["a", "aa"], ["aaa"]]
    assert sorted([sorted(sublist) for sublist in result]) == sorted(
        [sorted(sublist) for sublist in expected]
    )


def test_no_palindrome_except_single_chars(sol):
    s = "abc"
    result = sol.partition(s)
    expected = [["a", "b", "c"]]
    assert result == expected


def test_long_palindrome(sol):
    s = "racecar"
    result = sol.partition(s)
    # Not checking for all but basic correctness
    assert ["racecar"] in result


def test_mixed_case(sol):
    s = "aabaa"
    result = sol.partition(s)
    expected = [
        ["a", "a", "b", "a", "a"],
        ["aa", "b", "aa"],
        ["a", "aba", "a"],
        ["aabaa"],
    ]

    # Convert to tuple for hashable comparison
    result_set = set(tuple(p) for p in result)
    expected_set = set(tuple(p) for p in expected)

    # Each expected partition should be present in result
    for partition in expected_set:
        assert partition in result_set, f"Missing partition: {partition}"


def test_edge_case_empty(sol):
    s = ""
    result = sol.partition(s)
    expected = [[]]
    assert result == expected
