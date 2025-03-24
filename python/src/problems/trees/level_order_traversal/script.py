from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val=0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue: deque[TreeNode] = deque()

        if not root:
            return []

        queue.append(root)

        levels: list[list[int]] = []
        while queue:
            new_queue: deque[TreeNode] = deque()
            curr_level: list[int] = []

            for node in queue:
                curr_level.append(node.val)

                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

            levels.append(curr_level)
            queue = new_queue

        return levels
