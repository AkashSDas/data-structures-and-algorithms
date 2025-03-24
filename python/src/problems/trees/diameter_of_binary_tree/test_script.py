import pytest

from src.problems.trees.diameter_of_binary_tree.script import Solution, TreeNode


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
        ([1, 2, 3, 4, 5], 3),  # Example 1
        ([1, 2], 1),  # Example 2
        ([], 0),  # Empty tree
        ([1], 0),  # Single node
        ([1, 2, None, 3, None, 4, None], 3),  # Skewed left tree
    ],
)
def test_diameter_of_binary_tree(tree_list, expected):
    tree = build_tree_from_list(tree_list)
    assert Solution().diameterOfBinaryTree(tree) == expected
