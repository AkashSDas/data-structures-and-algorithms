import pytest

from src.problems.trees.balanced_binary_tree.script import Solution, TreeNode


def build_tree_from_list(vals):
    """Helper function to convert list to binary tree"""

    if not vals:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in vals]
    child_index = 1

    for node in nodes:
        if node:
            if child_index < len(nodes):
                node.left = nodes[child_index]
                child_index += 1
            if child_index < len(nodes):
                node.right = nodes[child_index]
                child_index += 1
    return nodes[0]


@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([3, 9, 20, None, None, 15, 7], True),  # Example 1: Balanced
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),  # Example 2: Not Balanced
        ([], True),  # Example 3: Empty tree (balanced)
        ([1], True),  # Single node (balanced)
        ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], False),  # Unbalanced deeper
    ],
)
def test_is_balanced(tree_list, expected):
    tree = build_tree_from_list(tree_list)
    assert Solution().isBalanced(tree) == expected
