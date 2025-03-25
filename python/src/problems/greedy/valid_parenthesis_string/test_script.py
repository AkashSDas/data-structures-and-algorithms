import pytest

from src.problems.greedy.valid_parenthesis_string.script import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),  # Example 1: Simple valid case
        ("(*)", True),  # Example 2: '*' acts as empty or '(' or ')'
        ("(*))", True),  # Example 3: '*' can be empty to balance
        ("(((((*)))))", True),  # Nested valid case
        ("((*)", True),  # '*' can act as ')'
        ("((*))", True),  # '*' acts as '('
        ("(((******)))", True),  # '*' can balance extra '('
        ("((*)))", True),  # '*' as '('
        ("(()))", False),  # Unbalanced: One extra ')'
        ("((((", False),  # Too many '(' with no closing ')'
        ("))))", False),  # Too many ')' with no opening '('
        ("(((((*))", False),  # Leftover '(' without match
        ("*)", True),  # '*' as '(' makes it valid
        ("(*", True),  # '*' as ')' makes it valid
        ("****", True),  # All '*' can be empty
        (")(", False),  # Wrong order, impossible to balance
        ("(*))(", False),  # Unbalanced, unmatched '('
    ],
)
def test_check_valid_string(s, expected):
    sol = Solution()
    assert sol.checkValidString(s) == expected
