import pytest
from copy import deepcopy

from src.problems.graph.course_schedule.script import Solution


@pytest.mark.parametrize(
    "numCourses, prerequisites, expected",
    [
        # Example cases
        (2, [[1, 0]], True),  # Possible
        (2, [[1, 0], [0, 1]], False),  # Cycle
        # No prerequisites (always possible)
        (3, [], True),
        # Single course, no prerequisites
        (1, [], True),
        # Multiple independent chains (possible)
        (4, [[1, 0], [3, 2]], True),
        # Larger cycle
        (4, [[1, 0], [2, 1], [3, 2], [0, 3]], False),
        # Complex graph, but possible
        (5, [[1, 0], [2, 0], [3, 1], [4, 3]], True),
        # Complex graph with cycle
        (5, [[1, 0], [2, 0], [3, 1], [4, 3], [1, 4]], False),
        # Large no-cycle case (stress test)
        (1000, [[i + 1, i] for i in range(999)], True),
        # Large cycle case (stress test)
        (1000, [[i + 1, i] for i in range(999)] + [[0, 999]], False),
    ],
)
def test_can_finish(numCourses, prerequisites, expected):
    sol = Solution()
    prereq_copy = deepcopy(prerequisites)  # Avoid mutating inputs
    assert sol.canFinish(numCourses, prereq_copy) == expected
