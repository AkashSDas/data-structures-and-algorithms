from typing import List, Optional

import pytest

from src.problems.trees.maximum_depth_of_binary_tree.script import Solution, TreeNode


# Helper function to convert list to tree
def list_to_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """Converts list to binary tree (level order)"""
    if not arr:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


@pytest.mark.parametrize(
    "input_list, expected_depth",
    [
        ([3, 9, 20, None, None, 15, 7], 3),  # Example 1
        ([1, None, 2], 2),  # Example 2
        ([], 0),  # Empty tree
        ([1], 1),  # Single node
        ([1, 2, 3, 4, None, None, 5], 3),  # Unbalanced tree
    ],
)
def test_max_depth(input_list, expected_depth):
    solution = Solution()
    root = list_to_tree(input_list)
    depth = solution.maxDepth(root)
    assert depth == expected_depth
