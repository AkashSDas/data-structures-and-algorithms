import pytest

from src.problems.heap_priority_queue.k_closest_point_to_origin.script import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    points = [[1, 3], [-2, 2]]
    k = 1
    expected = [[-2, 2]]
    result = solution.kClosest(points, k)
    assert sorted(result) == sorted(expected)


def test_example2(solution):
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    expected = [[3, 3], [-2, 4]]
    result = solution.kClosest(points, k)
    assert sorted(result) == sorted(expected)


def test_all_points_returned(solution):
    points = [[1, 2], [3, 4], [0, -1]]
    k = 3
    expected = [[1, 2], [3, 4], [0, -1]]
    result = solution.kClosest(points, k)
    assert sorted(result) == sorted(expected)


def test_negative_coordinates(solution):
    points = [[-3, -4], [-1, -1], [-2, -2]]
    k = 2
    expected = [[-1, -1], [-2, -2]]
    result = solution.kClosest(points, k)
    assert sorted(result) == sorted(expected)


def test_single_point(solution):
    points = [[0, 0]]
    k = 1
    expected = [[0, 0]]
    result = solution.kClosest(points, k)
    assert result == expected


def test_large_coordinates(solution):
    points = [[10000, 10000], [1, 2], [3, 4]]
    k = 2
    expected = [[1, 2], [3, 4]]
    result = solution.kClosest(points, k)
    assert sorted(result) == sorted(expected)


def test_zero_k(solution):
    points = [[1, 1], [2, 2]]
    k = 0
    expected = []
    result = solution.kClosest(points, k)
    assert result == expected


def test_same_distance(solution):
    points = [[0, 1], [1, 0]]
    k = 2
    expected = [[0, 1], [1, 0]]
    result = solution.kClosest(points, k)
    assert result == expected
