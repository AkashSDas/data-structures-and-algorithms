from typing import Optional
from collections import deque
import pytest

from src.problems.trees.lowest_common_ancestor_of_binary_search_tree.script import (
    Solution,
    TreeNode,
)


def build_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    """Helper to build tree from level-order list."""

    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while queue and i < len(lst):
        node = queue.popleft()

        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1

    return root


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Finds node with given value in BST."""

    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return find_node(root.left, val)
    else:
        return find_node(root.right, val)


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 8)
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 6


def test_example2(solution):
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = find_node(root, 2)
    q = find_node(root, 4)
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 2


def test_example3(solution):
    root = build_tree([2, 1])
    p = find_node(root, 2)
    q = find_node(root, 1)
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 2


def test_lca_is_root(solution):
    root = build_tree([5, 3, 7, 2, 4, 6, 8])
    p = find_node(root, 3)
    q = find_node(root, 7)
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 5


def test_lca_same_node(solution):
    root = build_tree([5, 3, 7])
    p = find_node(root, 3)
    q = find_node(root, 3)
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 3
