import pytest
from typing import List, Optional

from src.problems.graph.clone_graph.script import Node, Solution


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None

    nodes = {}
    for i in range(1, len(adj_list) + 1):
        nodes[i] = Node(i)

    for idx, neighbors in enumerate(adj_list, start=1):
        nodes[idx].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []

    visited = {}
    result = {}

    def dfs(n: Node):
        if n.val in visited:
            return
        visited[n.val] = n
        result[n.val] = [neighbor.val for neighbor in n.neighbors]
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)
    return [sorted(result[i]) for i in sorted(result)]


@pytest.mark.parametrize(
    "adj_list, expected",
    [
        (
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 4], [1, 3], [2, 4], [1, 3]],
        ),  # Example 1
        ([[]], [[]]),  # Example 2: Single node no neighbors
        ([], []),  # Example 3: Empty graph
        ([[2], [1]], [[2], [1]]),  # Simple 2-node connected graph
        ([[2, 3], [1, 3], [1, 2]], [[2, 3], [1, 3], [1, 2]]),  # Triangle graph
    ],
)
def test_clone_graph(adj_list, expected):
    solution = Solution()
    original = build_graph(adj_list)
    cloned = solution.cloneGraph(original)
    cloned_adj_list = graph_to_adj_list(cloned)
    assert cloned_adj_list == expected
