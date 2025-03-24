from typing import List, Optional

import pytest

from src.problems.trees.invert_binary_tree.script import Solution, TreeNode


# Helper functions for testing
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


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts binary tree to list (level order)"""

    if not root:
        return []

    result = []
    queue: List[Optional[TreeNode]] = [root]

    while any(queue):
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ],
)
def test_invert_tree(input_list, expected_output):
    solution = Solution()
    root = list_to_tree(input_list)
    inverted_root = solution.invertTree(root)
    output_list = tree_to_list(inverted_root)
    assert output_list == expected_output
