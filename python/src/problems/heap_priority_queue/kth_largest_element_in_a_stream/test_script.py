from src.problems.heap_priority_queue.kth_largest_element_in_a_stream.script import (
    KthLargest,
)


def test_kth_largest_case1():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8


def test_kth_largest_case2():
    kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert kthLargest.add(2) == 7
    assert kthLargest.add(10) == 7
    assert kthLargest.add(9) == 7
    assert kthLargest.add(9) == 8


def test_kth_largest_small():
    kthLargest = KthLargest(1, [1])
    assert kthLargest.add(0) == 1
    assert kthLargest.add(2) == 2
    assert kthLargest.add(-1) == 2


def test_kth_largest_large_k():
    kthLargest = KthLargest(5, [10, 7, 11, 5])
    assert kthLargest.add(6) == 5
    assert kthLargest.add(4) == 5
    assert kthLargest.add(12) == 6


def test_kth_largest_duplicates():
    kthLargest = KthLargest(2, [2, 2, 2])
    assert kthLargest.add(2) == 2
    assert kthLargest.add(3) == 2
    assert kthLargest.add(4) == 3
