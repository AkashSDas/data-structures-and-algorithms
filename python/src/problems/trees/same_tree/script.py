from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int | None = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


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
