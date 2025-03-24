import pytest

from src.problems.arrays_and_hashing.product_of_array_except_self.script import Solution


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 1, 2, 3], [6, 0, 0, 0]),
        ([-1, -2, -3, -4], [-24, -12, -8, -6]),
        (
            [5],
            [5],
        ),
    ],
)
def test_product_except_self(input_data, expected_output):
    solution = Solution()
    assert solution.productExceptSelf(input_data) == expected_output
