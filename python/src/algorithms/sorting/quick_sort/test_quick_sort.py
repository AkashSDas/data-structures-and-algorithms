from typing import List

from src.algorithms.sorting.quick_sort.quick_sort import quick_sort, partition


def test_quick_sort_basic():
    arr = [3, 6, 1, 5, 9, 8]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)


def test_quick_sort_empty():
    arr: List[int] = []
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == []


def test_quick_sort_single_element():
    arr = [1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1]


def test_quick_sort_sorted():
    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]


def test_quick_sort_reverse_sorted():
    arr = [9, 7, 5, 3, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 3, 5, 7, 9]


def test_quick_sort_duplicates():
    arr = [4, 2, 5, 2, 3, 2]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)


def test_quick_sort_large_numbers():
    arr = [100000, 99999, 123456, 987654, 123]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == sorted(arr)


def test_partition_correctness():
    arr = [4, 2, 7, 1, 3]
    pivot_index = partition(arr, 0, len(arr) - 1)
    pivot_value = arr[pivot_index]

    # Check if elements to left are <= pivot and right are >= pivot
    left = arr[:pivot_index]
    right = arr[pivot_index + 1 :]

    assert all(x <= pivot_value for x in left)
    assert all(x >= pivot_value for x in right)
