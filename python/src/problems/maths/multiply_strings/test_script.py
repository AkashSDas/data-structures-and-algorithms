import pytest

from src.problems.maths.multiply_strings.script import Solution


@pytest.fixture
def solver():
    return Solution()


def test_simple_multiplication(solver):
    assert solver.multiply("2", "3") == "6"


def test_multiplying_with_zero(solver):
    assert solver.multiply("0", "123") == "0"
    assert solver.multiply("123", "0") == "0"


def test_single_digit_multiplication(solver):
    assert solver.multiply("9", "9") == "81"


def test_large_numbers(solver):
    assert solver.multiply("123", "456") == "56088"
    assert solver.multiply("999", "999") == "998001"


def test_one_multiplicand_is_one(solver):
    assert solver.multiply("1", "789") == "789"
    assert solver.multiply("789", "1") == "789"


def test_edge_case_min_length(solver):
    assert solver.multiply("1", "1") == "1"


def test_max_length_inputs(solver):
    num1 = "9" * 200
    num2 = "9" * 200
    result = solver.multiply(num1, num2)
    assert (
        result.startswith("9") and len(result) == 400 or len(result) == 399
    )  # Approximate shape check
