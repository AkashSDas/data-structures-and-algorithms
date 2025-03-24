from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int | None = 0, left=None, right=None):
        self.val: int | None = val
        self.left: "TreeNode | None" = left
        self.right: "TreeNode | None" = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        p_queue: deque[TreeNode] = deque()
        q_queue: deque[TreeNode] = deque()

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if p_node.val != q_node.val:
                return False

            # Check left
            if (p_node.left is None) != (q_node.left is None):
                return False
            if p_node.left and q_node.left:
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)

            # Check right
            if (p_node.right is None) != (q_node.right is None):
                return False
            if p_node.right and q_node.right:
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)

        return not p_queue and not q_queue

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        same_value_nodes: list[TreeNode] = []

        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False

        queue: deque[TreeNode] = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.val == subRoot.val:
                same_value_nodes.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not same_value_nodes:
            return False

        for node in same_value_nodes:
            if self.isSameTree(node, subRoot):
                return True

        return False
