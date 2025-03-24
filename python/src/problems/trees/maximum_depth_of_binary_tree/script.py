from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increment_height(self, node: TreeNode, height: int, levels: list[int]) -> None:
        levels.append(height)

        if node.left:
            self.increment_height(node.left, height + 1, levels)
        if node.right:
            self.increment_height(node.right, height + 1, levels)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        levels: list[int] = []

        if root:
            self.increment_height(root, 1, levels)

        return max(levels) if len(levels) > 0 else 0

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
