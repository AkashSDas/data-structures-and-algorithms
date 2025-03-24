from src.problems.heap_priority_queue.find_median_from_data_stream.script import (
    MedianFinder,
)


def test_basic_example():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0


def test_single_element():
    mf = MedianFinder()
    mf.addNum(10)
    assert mf.findMedian() == 10


def test_even_number_elements():
    mf = MedianFinder()
    mf.addNum(5)
    mf.addNum(15)
    mf.addNum(1)
    mf.addNum(3)
    assert mf.findMedian() == (3 + 5) / 2  # Median is average of 3 and 5


def test_odd_number_elements():
    mf = MedianFinder()
    mf.addNum(2)
    mf.addNum(4)
    mf.addNum(6)
    assert mf.findMedian() == 4


def test_negative_numbers():
    mf = MedianFinder()
    mf.addNum(-5)
    mf.addNum(-10)
    mf.addNum(-1)
    assert mf.findMedian() == -5


def test_large_numbers():
    mf = MedianFinder()
    nums = [10**5, -(10**5), 0, 99999, -99999]
    for num in nums:
        mf.addNum(num)
    assert mf.findMedian() == 0


def test_incremental_median():
    mf = MedianFinder()
    arr = [7, 1, 3, 5, 9]
    expected = [7, 4.0, 3, 4.0, 5]
    for i, num in enumerate(arr):
        mf.addNum(num)
        assert mf.findMedian() == expected[i]
