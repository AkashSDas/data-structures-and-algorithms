import pytest

from src.problems.heap_priority_queue.task_scheduler.script import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    expected = 8
    assert solution.leastInterval(tasks, n) == expected


def test_example2(solution):
    tasks = ["A", "C", "A", "B", "D", "B"]
    n = 1
    expected = 6
    assert solution.leastInterval(tasks, n) == expected


def test_example3(solution):
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 3
    expected = 10
    assert solution.leastInterval(tasks, n) == expected


def test_no_cooling(solution):
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    expected = 6  # No cooling, tasks can run one after another
    assert solution.leastInterval(tasks, n) == expected


def test_single_task(solution):
    tasks = ["A"]
    n = 100
    expected = 1  # Only one task, no idling needed
    assert solution.leastInterval(tasks, n) == expected


def test_all_unique_tasks(solution):
    tasks = ["A", "B", "C", "D", "E", "F"]
    n = 3
    expected = 6  # All unique tasks, no idles needed
    assert solution.leastInterval(tasks, n) == expected


def test_large_gap_needed(solution):
    tasks = ["A", "A", "A", "A"]
    n = 3
    expected = 13  # A -> idle -> idle -> idle -> A -> idle -> idle -> idle -> A -> idle -> idle -> idle -> A
    assert solution.leastInterval(tasks, n) == expected
