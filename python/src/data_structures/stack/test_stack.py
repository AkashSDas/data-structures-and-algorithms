from src.data_structures.stack.stack import Stack


def test_push_and_to_list():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.to_list() == [3, 2, 1]
    assert s.size == 3


def test_pop():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    node = s.pop()
    assert node is not None
    assert node.val == 30
    assert s.to_list() == [20, 10]
    assert s.size == 2

    s.pop()
    s.pop()
    # Now empty
    assert s.pop() is None
    assert s.to_list() == []
    assert s.size == 0


def test_peek():
    s = Stack()
    assert s.peek() is None  # Empty stack

    s.push(99)
    peek_node = s.peek()
    assert peek_node is not None
    assert peek_node.val == 99
    assert s.size == 1


def test_find():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    found = s.find(2)
    assert found is not None
    assert found.val == 2

    not_found = s.find(999)
    assert not_found is None


def test_iterable():
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(7)

    vals = [node.val for node in s]
    assert vals == [7, 6, 5]


def test_empty_pop_and_iter():
    s = Stack()
    # Pop on empty
    assert s.pop() is None
    # Iterate empty
    vals = [node.val for node in s]
    assert vals == []
