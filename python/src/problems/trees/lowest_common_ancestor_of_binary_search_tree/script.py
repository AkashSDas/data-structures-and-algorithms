# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


class Solution:
    def find_path(
        self,
        node: TreeNode | None,
        target: TreeNode,
        path: list[TreeNode],
    ) -> bool:
        if not node:
            return False

        path.append(node)

        if node.val == target.val:
            return True

        if node.val > target.val:
            if self.find_path(node.left, target, path):
                return True
        else:
            if self.find_path(node.right, target, path):
                return True

        # Backtrack
        path.pop()
        return False

    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        p_path: list[TreeNode] = []
        q_path: list[TreeNode] = []

        self.find_path(root, p, p_path)
        self.find_path(root, q, q_path)

        # Compare paths
        lca = None
        for u, v in zip(p_path, q_path):
            if u.val == v.val:
                lca = u
            else:
                break

        assert lca is not None
        return lca
