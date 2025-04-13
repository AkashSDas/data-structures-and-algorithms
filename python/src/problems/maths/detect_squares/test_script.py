from src.problems.maths.detect_squares.script import DetectSquares


def test_basic_square_detection():
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    assert ds.count([11, 10]) == 1  # One square can be formed


def test_no_square_possible():
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    assert ds.count([14, 8]) == 0  # No square possible with this point


def test_duplicate_points_increase_count():
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    ds.add([11, 2])  # duplicate point
    assert ds.count([11, 10]) == 2  # Two squares now due to duplicate


def test_multiple_squares():
    ds = DetectSquares()
    ds.add([1, 1])
    ds.add([1, 3])
    ds.add([3, 1])
    ds.add([3, 3])
    assert ds.count([1, 1]) == 1
    assert ds.count([3, 3]) == 1
    assert ds.count([2, 2]) == 0  # Not a square corner
    ds.add([1, 3])  # Duplicate point
    assert ds.count([3, 1]) == 2  # Now two squares


def test_no_points():
    ds = DetectSquares()
    assert ds.count([5, 5]) == 0


def test_far_apart_points():
    ds = DetectSquares()
    ds.add([0, 0])
    ds.add([1000, 0])
    ds.add([0, 1000])
    ds.add([1000, 1000])
    assert ds.count([0, 0]) == 1
    assert ds.count([500, 500]) == 0
