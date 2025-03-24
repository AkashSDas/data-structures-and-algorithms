import pytest

from src.problems.stack.valid_parentheses.script import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),  # Simple valid case
        ("()[]{}", True),  # Multiple valid brackets
        ("(]", False),  # Mismatched brackets
        ("([)]", False),  # Incorrect nesting
        ("{[]}", True),  # Nested correctly
        ("", True),  # Empty string is valid
        ("(", False),  # Single opening bracket
        (")", False),  # Single closing bracket
        ("(()", False),  # Unclosed bracket
        ("([{}])", True),  # Deeply nested valid case
    ],
)
def test_isValid(s, expected):
    solution = Solution()
    assert solution.isValid(s) == expected
