import pytest

from src.problems.graph.course_schedule_2.script import Solution


# Pytest Cases
@pytest.mark.parametrize(
    "numCourses, prerequisites, expected_valid_orders",
    [
        # Case 1: Simple linear dependency
        (2, [[1, 0]], [[0, 1]]),
        # Case 2: No prerequisites
        (1, [], [[0]]),
        # Case 3: Multiple valid orders
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [[0, 1, 2, 3], [0, 2, 1, 3]]),
        # Case 4: Impossible due to cycle
        (2, [[1, 0], [0, 1]], [[]]),
        # Case 5: Larger case
        (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]], [[0, 1, 2, 3, 4, 5]]),
        # Case 6: Disconnected courses
        (
            3,
            [],
            [[0, 1, 2], [1, 0, 2], [2, 1, 0], [2, 0, 1], [1, 2, 0], [0, 2, 1]],
        ),  # Any order
    ],
)
def test_findOrder(numCourses, prerequisites, expected_valid_orders):
    sol = Solution()
    result = sol.findOrder(numCourses, prerequisites)
    if [] in expected_valid_orders:
        assert result == [], f"Expected [], got {result}"
    else:
        # Check if result is one of the valid orderings
        assert (
            result in expected_valid_orders
        ), f"Expected one of {expected_valid_orders}, got {result}"
