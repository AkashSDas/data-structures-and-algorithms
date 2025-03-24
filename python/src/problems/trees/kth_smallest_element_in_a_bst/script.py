# Definition for a binary tree node.
import heapq
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: "TreeNode |None" = None,
        right: "TreeNode |None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.heap: list[int] = []

    def traverse(self, node: Optional[TreeNode], k: int) -> None:
        if not node:
            return

        if len(self.heap) < k:
            heapq.heappush(self.heap, -node.val)
        elif len(self.heap) == k:
            max_val = heapq.heappop(self.heap)
            if -max_val > node.val:
                heapq.heappush(self.heap, -node.val)
            else:
                heapq.heappush(self.heap, max_val)
        else:
            raise Exception("Heap more than full")  # Shouldn't reach here

        self.traverse(node.left, k)
        self.traverse(node.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        self.traverse(root, k)

        return -heapq.heappop(self.heap)
