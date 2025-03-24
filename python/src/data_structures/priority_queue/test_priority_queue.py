from src.data_structures.priority_queue.priority_queue import PriorityQueue


def test_insert_and_peek():
    pq = PriorityQueue()
    pq.insert(5)
    assert pq.peek() == 5

    pq.insert(3)
    assert pq.peek() == 3  # Min-heap property

    pq.insert(7)
    assert pq.peek() == 3


def test_length():
    pq = PriorityQueue()
    assert len(pq) == 0

    pq.insert(1)
    pq.insert(2)
    assert len(pq) == 2


def test_remove_single_element():
    pq = PriorityQueue()
    pq.insert(4)
    pq.insert(2)
    pq.insert(6)

    pq.remove(2)
    assert 2 not in pq.heap
    assert pq.peek() == 4


def test_remove_duplicates():
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(5)
    pq.insert(3)
    pq.insert(1)
    pq.insert(3)

    pq.remove(3)
    assert pq.heap.count(3) == 0
    assert pq.peek() == 1


def test_remove_nonexistent_value():
    pq = PriorityQueue()
    pq.insert(1)
    pq.insert(2)

    pq.remove(10)  # Should not fail
    assert pq.heap == [1, 2]


def test_remove_from_empty_queue():
    pq = PriorityQueue()
    pq.remove(5)
    assert len(pq) == 0


def test_peek_empty_queue():
    pq = PriorityQueue()
    assert pq.peek() is None


def test_heap_property_after_multiple_operations():
    pq = PriorityQueue()
    nums = [10, 4, 7, 1, 8, 3]
    for num in nums:
        pq.insert(num)

    assert pq.peek() == 1

    pq.remove(1)
    assert pq.peek() == 3

    pq.insert(2)
    assert pq.peek() == 2

    pq.remove(2)
    assert pq.peek() == 3


def test_get_indexes():
    pq = PriorityQueue()
    pq.insert(5)
    pq.insert(1)
    pq.insert(5)
    pq.insert(3)

    indexes = pq.get_indexes(5)
    assert len(indexes) == 2
    assert all(pq.heap[i] == 5 for i in indexes)
