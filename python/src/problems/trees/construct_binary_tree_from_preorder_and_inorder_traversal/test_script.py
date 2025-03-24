import pytest
from typing import Optional

from src.problems.trees.construct_binary_tree_from_preorder_and_inorder_traversal.script import (
    TreeNode,
    Solution,
)


# Function to compare two binary trees
def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (
        p.val == q.val
        and is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )


# Helper to build tree from list (for expected output)
def build_tree_from_list(vals):
    if not vals:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in vals]

    child_index = 1
    for i in range(len(nodes)):
        node = nodes[i]
        if node is not None:
            if child_index < len(nodes):
                node.left = nodes[child_index]
                child_index += 1
            if child_index < len(nodes):
                node.right = nodes[child_index]
                child_index += 1
    return nodes[0]


@pytest.mark.parametrize(
    "preorder, inorder, expected_list",
    [
        (
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            [3, 9, 20, None, None, 15, 7],
        ),  # Example 1
        ([-1], [-1], [-1]),  # Example 2 (single node)
        ([1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [1, 2, 3, 4, 5]),  # Custom test
        ([1, 2, 3], [2, 1, 3], [1, 2, 3]),  # Simple balanced
        ([1], [1], [1]),  # Single node again
    ],
)
def test_build_tree(preorder, inorder, expected_list):
    sol = Solution()
    built_tree = sol.buildTree(preorder.copy(), inorder.copy())
    expected_tree = build_tree_from_list(expected_list)
    assert is_same_tree(built_tree, expected_tree)
