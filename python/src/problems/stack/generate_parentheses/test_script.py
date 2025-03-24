import pytest

from src.problems.stack.generate_parentheses.script import Solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
        ),
    ],
)
def test_generate_parenthesis(n, expected):
    solution = Solution()
    result = solution.generateParenthesis(n)

    # Convert lists to sets for order-independent comparison
    assert set(result) == set(expected)


def test_generate_parenthesis_empty():
    solution = Solution()
    assert solution.generateParenthesis(0) == []  # Edge case: n = 0


def test_generate_parenthesis_large():
    solution = Solution()
    result = solution.generateParenthesis(5)

    # Check if the number of combinations matches the known count for n=5
    assert len(result) == 42  # There are 42 valid combinations for n=5
