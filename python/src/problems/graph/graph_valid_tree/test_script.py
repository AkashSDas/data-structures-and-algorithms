import pytest

from src.problems.graph.graph_valid_tree.script import Solution


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),  # Valid tree
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),  # Cycle present
        (4, [[0, 1], [2, 3]], False),  # Disconnected
        (1, [], True),  # Single node, valid tree
        (2, [[0, 1]], True),  # Simple valid tree
        (2, [[0, 1], [1, 0]], False),  # Extra redundant edge (cycle)
    ],
)
def test_validTree(n, edges, expected):
    sol = Solution()
    assert sol.validTree(n, edges) == expected
