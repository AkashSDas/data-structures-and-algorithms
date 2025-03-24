import pytest

from src.problems.two_pointers.valid_palindrome.script import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        (
            "A man, a plan, a canal: Panama",
            True,
        ),  # Valid palindrome with special characters
        ("racecar", True),  # Simple palindrome
        ("No lemon, no melon", True),  # Palindrome with spaces and mixed cases
        ("Hello, world!", False),  # Not a palindrome
        ("Was it a car or a cat I saw?", True),  # Valid palindrome with punctuation
        ("", True),  # Empty string is a valid palindrome
        ("12321", True),  # Numeric palindrome
        ("12345", False),  # Non-palindromic number
    ],
)
def test_is_palindrome(s: str, expected: bool):
    solution = Solution()
    assert solution.isPalindrome(s) == expected
