import pytest

from src.problems.trees.validate_binary_search_tree.script import Solution, TreeNode


# Helper function to build a binary tree from list
def build_tree(nodes):
    if not nodes:
        return None

    node_list = []
    for val in nodes:
        node = TreeNode(val) if val is not None else None
        node_list.append(node)

    kids = node_list[::-1]
    root = kids.pop()

    for node in node_list:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


# Pytest test cases
@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([2, 1, 3], True),  # Example 1: Valid BST
        ([5, 1, 4, None, None, 3, 6], False),  # Example 2: Invalid BST
        ([1, 1], False),  # Duplicate values not allowed in BST
        ([10, 5, 15, None, None, 6, 20], False),  # Invalid right subtree
        ([3, 1, 5, 0, 2, 4, 6], True),  # Perfect BST
        ([2147483647], True),  # Single node with max int value
        ([0, None, -1], False),  # Invalid BST (right child < root)
        ([], True),  # Empty tree is valid BST
    ],
)
def test_is_valid_bst(tree_list, expected):
    root = build_tree(tree_list)
    sol = Solution()
    assert sol.isValidBST(root) == expected
