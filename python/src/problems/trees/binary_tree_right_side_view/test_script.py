import pytest

from src.problems.trees.binary_tree_right_side_view.script import Solution, TreeNode


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
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),  # Example 1
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),  # Example 2
        ([1, None, 3], [1, 3]),  # Example 3
        ([], []),  # Example 4
        ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),  # Left-skewed tree
    ],
)
def test_right_side_view(tree_list, expected):
    root = build_tree(tree_list)
    sol = Solution()
    assert sol.rightSideView(root) == expected
