import pytest

from src.problems.backtracking.n_queens.script import Solution


@pytest.fixture
def sol():
    return Solution()


def test_example_case_n4(sol):
    n = 4
    expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    result = sol.solveNQueens(n)
    # Convert both to sets for order-independent comparison
    assert set(tuple(row for row in solution) for solution in result) == set(
        tuple(row for row in solution) for solution in expected
    )


def test_single_queen(sol):
    n = 1
    expected = [["Q"]]
    result = sol.solveNQueens(n)
    assert result == expected


def test_two_queens(sol):
    n = 2
    # No solution exists for n=2
    result = sol.solveNQueens(n)
    assert result == []


def test_three_queens(sol):
    n = 3
    # No solution exists for n=3
    result = sol.solveNQueens(n)
    assert result == []


def test_n5_solution_count(sol):
    n = 5
    result = sol.solveNQueens(n)
    # There are exactly 10 distinct solutions for 5-queens
    assert len(result) == 10
    # Validate board size and queen count per board
    for board in result:
        assert len(board) == n
        for row in board:
            assert row.count("Q") == 1
        # Check total queens per board
        assert sum(row.count("Q") for row in board) == n


def test_n6_solution_count(sol):
    n = 6
    result = sol.solveNQueens(n)
    # 4-Queens has 4 solutions
    # 6-Queens has 4 solutions
    assert len(result) == 4
    for board in result:
        assert len(board) == n
        for row in board:
            assert row.count("Q") == 1
