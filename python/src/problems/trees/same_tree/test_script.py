from typing import Optional
import pytest
from collections import deque

from src.problems.trees.same_tree.script import Solution, TreeNode


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from level-order list with None representing null."""

    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


@pytest.mark.parametrize(
    "tree1, tree2, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),  # Example 1 - Same
        ([1, 2], [1, None, 2], False),  # Example 2 - Structure different
        ([1, 2, 1], [1, 1, 2], False),  # Example 3 - Values different
        ([], [], True),  # Both empty trees
        ([1], [1], True),  # Single node same
        ([1, 2, 3], [1, 2, 4], False),  # Same structure, different value
        ([1, 2, None], [1, None, 2], False),  # Same values, different structure
    ],
)
def test_isSameTree(tree1, tree2, expected):
    root1 = build_tree(tree1)
    root2 = build_tree(tree2)
    sol = Solution()
    assert sol.isSameTree(root1, root2) == expected
