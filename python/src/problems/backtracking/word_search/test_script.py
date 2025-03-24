import pytest

from src.problems.backtracking.word_search.script import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert solution.exist(board, word) is True


def test_example2(solution):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    assert solution.exist(board, word) is True


def test_example3(solution):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    assert solution.exist(board, word) is False


def test_single_letter_true(solution):
    board = [["A"]]
    word = "A"
    assert solution.exist(board, word) is True


def test_single_letter_false(solution):
    board = [["A"]]
    word = "B"
    assert solution.exist(board, word) is False


def test_multiple_paths(solution):
    board = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    word = "AEI"
    assert solution.exist(board, word) is False  # Diagonal not allowed


def test_reuse_same_cell(solution):
    board = [["A", "A", "A"], ["A", "A", "A"], ["A", "A", "A"]]
    word = "AAAAAAAAA"
    assert solution.exist(board, word) is True  # Uses all cells once, allowed


def test_case_sensitivity(solution):
    board = [["a", "b"], ["C", "D"]]
    word = "bC"
    assert solution.exist(board, word) is False
