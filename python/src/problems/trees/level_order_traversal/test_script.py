import pytest

from src.problems.trees.level_order_traversal.script import (
    TreeNode,
    Solution,
)


def build_tree(values):
    """
    Helper function to build a binary tree from a list, treating None as empty nodes.
    """

    if not values:
        return None

    nodes = []
    for val in values:
        node = TreeNode(val) if val is not None else None
        nodes.append(node)

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
    "tree_list, expected",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
    ],
)
def test_level_order(tree_list, expected):
    root = build_tree(tree_list)
    sol = Solution()
    assert sol.levelOrder(root) == expected
