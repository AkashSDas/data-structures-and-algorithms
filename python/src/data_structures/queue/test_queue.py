from src.data_structures.queue.queue import Queue


def test_enqueue_and_to_list():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.to_list() == [1, 2, 3]
    assert len(q) == 3


def test_dequeue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    node = q.dequeue()
    assert node is not None
    assert node.val == 10
    assert q.to_list() == [20, 30]
    assert len(q) == 2

    q.dequeue()
    q.dequeue()
    # Now empty
    assert q.dequeue() is None
    assert q.to_list() == []
    assert len(q) == 0


def test_peek():
    q = Queue()
    assert q.peek() is None  # Empty queue

    q.enqueue(99)
    peek_node = q.peek()
    assert peek_node is not None
    assert peek_node.val == 99
    assert len(q) == 1


def test_find():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    found = q.find(2)
    assert found is not None
    assert found.val == 2

    not_found = q.find(999)
    assert not_found is None


def test_iterable():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)

    vals = [node.val for node in q]
    assert vals == [5, 6, 7]


def test_len_dunder():
    q = Queue()
    assert len(q) == 0
    q.enqueue(1)
    assert len(q) == 1
    q.dequeue()
    assert len(q) == 0
