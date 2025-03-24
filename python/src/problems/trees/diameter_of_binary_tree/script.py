from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.max = 0

    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_depth = self.get_height(node.left)
        right_depth = self.get_height(node.right)

        if (left_depth + right_depth) > self.max:
            self.max = left_depth + right_depth

        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_height(root)
        return self.max
