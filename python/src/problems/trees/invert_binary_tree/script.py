# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def swap(self, node: TreeNode) -> None:
        right_node = node.right
        node.right = node.left
        node.left = right_node

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        node = root

        if not node:
            return node

        if node.left:
            self.invertTree(node.left)
        if node.right:
            self.invertTree(node.right)

        self.swap(node)
        return node
