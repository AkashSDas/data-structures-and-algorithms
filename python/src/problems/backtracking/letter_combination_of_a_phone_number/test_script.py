import pytest

from src.problems.backtracking.letter_combination_of_a_phone_number.script import (
    Solution,
)


@pytest.fixture
def sol():
    return Solution()


def test_example_case_1(sol):
    digits = "23"
    expected = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    result = sorted(sol.letterCombinations(digits))
    assert result == expected


def test_example_case_2_empty_input(sol):
    digits = ""
    expected = []
    result = sol.letterCombinations(digits)
    assert result == expected


def test_example_case_3_single_digit(sol):
    digits = "2"
    expected = sorted(["a", "b", "c"])
    result = sorted(sol.letterCombinations(digits))
    assert result == expected


def test_two_same_digits(sol):
    digits = "22"
    expected = sorted(["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"])
    result = sorted(sol.letterCombinations(digits))
    assert result == expected


def test_long_input(sol):
    digits = "234"
    expected = sorted([a + b + c for a in "abc" for b in "def" for c in "ghi"])
    result = sorted(sol.letterCombinations(digits))
    assert result == expected


def test_max_length_input(sol):
    digits = "2794"
    result = sol.letterCombinations(digits)
    # Check that all combinations have correct length
    assert all(len(combo) == len(digits) for combo in result)
    # Check no duplicate combinations
    assert len(result) == len(set(result))
