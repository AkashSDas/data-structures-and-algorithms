import pytest

from src.problems.stack.min_stack.script import MinStack


def test_min_stack():
    min_stack = MinStack()

    # Test push operations
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    # Test getMin()
    assert min_stack.getMin() == -3  # Minimum should be -3

    # Test pop() and re-check getMin()
    min_stack.pop()
    assert min_stack.top() == 0  # Top element should now be 0
    assert min_stack.getMin() == -2  # Minimum should be -2


def test_push_and_min():
    min_stack = MinStack()

    min_stack.push(3)
    assert min_stack.getMin() == 3  # Only one element, min = 3

    min_stack.push(5)
    assert min_stack.getMin() == 3  # Min remains 3

    min_stack.push(2)
    assert min_stack.getMin() == 2  # New min is 2

    min_stack.push(1)
    assert min_stack.getMin() == 1  # New min is 1


def test_pop_and_min():
    min_stack = MinStack()

    min_stack.push(3)
    min_stack.push(2)
    min_stack.push(1)

    assert min_stack.getMin() == 1  # Min is 1

    min_stack.pop()
    assert min_stack.getMin() == 2  # Min is now 2

    min_stack.pop()
    assert min_stack.getMin() == 3  # Min is now 3

    min_stack.pop()
    with pytest.raises(AssertionError):
        min_stack.getMin()  # Should raise an error since stack is empty


def test_top():
    min_stack = MinStack()

    min_stack.push(10)
    assert min_stack.top() == 10  # Top should be 10

    min_stack.push(20)
    assert min_stack.top() == 20  # Top should be 20

    min_stack.pop()
    assert min_stack.top() == 10  # Top should be back to 10


def test_empty_stack():
    min_stack = MinStack()

    with pytest.raises(
        IndexError
    ):  # Should raise an error when popping from an empty stack
        min_stack.pop()

    with pytest.raises(
        IndexError
    ):  # Should raise an error when getting top from an empty stack
        min_stack.top()

    with pytest.raises(
        AssertionError
    ):  # Should raise an error when getting min from an empty stack
        min_stack.getMin()
