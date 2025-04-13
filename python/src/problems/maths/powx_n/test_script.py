import pytest

from src.problems.maths.powx_n.script import Solution


@pytest.fixture
def solver():
    return Solution()


def test_positive_power(solver):
    assert pytest.approx(solver.myPow(2.0, 10), rel=1e-9) == 1024.0


def test_zero_power(solver):
    assert pytest.approx(solver.myPow(2.0, 0), rel=1e-9) == 1.0


def test_one_power(solver):
    assert pytest.approx(solver.myPow(5.0, 1), rel=1e-9) == 5.0


def test_negative_power(solver):
    assert pytest.approx(solver.myPow(2.0, -2), rel=1e-9) == 0.25


def test_fractional_base(solver):
    assert pytest.approx(solver.myPow(0.5, 3), rel=1e-9) == 0.125


def test_zero_base_nonzero_exp(solver):
    assert pytest.approx(solver.myPow(0.0, 5), rel=1e-9) == 0.0


def test_large_exponent(solver):
    assert pytest.approx(solver.myPow(1.00001, 123456), rel=1e-5) == pow(
        1.00001, 123456
    )


def test_negative_exponent_large(solver):
    assert pytest.approx(solver.myPow(2.0, -100), rel=1e-9) == pow(2.0, -100)
