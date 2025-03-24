import pytest

from src.problems.trees.count_good_nodes_in_binary_tree.script import TreeNode, Solution


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
        ([3, 1, 4, 3, None, 1, 5], 4),  # Example 1
        ([3, 3, None, 4, 2], 3),  # Example 2
        ([1], 1),  # Example 3
        ([2, 2, 2, 2, 2, 2, 2], 7),  # All same values (all good)
        ([5, 4, 6, 3, None, None, 7], 3),  # Corrected expected value to 3
        ([], 0),  # Empty tree
    ],
)
def test_good_nodes(tree_list, expected):
    root = build_tree(tree_list)
    sol = Solution()
    assert sol.goodNodes(root) == expected
