from typing import Optional, List
import pytest

from src.problems.trees.kth_smallest_element_in_a_bst.script import Solution, TreeNode


# Function to build tree from list input
def build_tree_from_list(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


# Test cases
@pytest.mark.parametrize(
    "tree_list, k, expected",
    [
        ([3, 1, 4, None, 2], 1, 1),  # Example 1
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),  # Example 2
        ([2, 1, 3], 2, 2),  # Simple case
        ([1], 1, 1),  # Single node
        ([3, 1, 4, None, 2], 3, 3),  # Third smallest
        ([5, 3, 6, 2, 4, None, None, 1], 1, 1),  # First smallest
    ],
)
def test_kth_smallest(tree_list, k, expected):
    root = build_tree_from_list(tree_list)
    sol = Solution()
    assert sol.kthSmallest(root, k) == expected
