import pytest
from typing import Optional
from collections import deque

from src.problems.trees.subtree_of_another_tree.script import Solution, TreeNode


def build_tree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    """Helper to build a tree from level-order list"""

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


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    root = build_tree([3, 4, 5, 1, 2])
    subRoot = build_tree([4, 1, 2])
    assert solution.isSubtree(root, subRoot) is True


def test_example2(solution):
    root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = build_tree([4, 1, 2])
    assert solution.isSubtree(root, subRoot) is False


def test_same_tree(solution):
    root = build_tree([1, 2, 3])
    subRoot = build_tree([1, 2, 3])
    assert solution.isSubtree(root, subRoot) is True


def test_subtree_single_node(solution):
    root = build_tree([1, 2, 3])
    subRoot = build_tree([2])
    assert solution.isSubtree(root, subRoot) is True


def test_empty_subtree(solution):
    root = build_tree([1, 2, 3])
    subRoot = build_tree([])
    assert solution.isSubtree(root, subRoot) is False


def test_empty_root(solution):
    root = build_tree([])
    subRoot = build_tree([1])
    assert solution.isSubtree(root, subRoot) is False
