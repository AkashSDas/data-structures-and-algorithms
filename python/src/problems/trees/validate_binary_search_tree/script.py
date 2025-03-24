from typing import Optional


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


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            return dfs(node.left, min_val, node.val) and dfs(
                node.right, node.val, max_val
            )

        return dfs(root, float("-inf"), float("inf"))
