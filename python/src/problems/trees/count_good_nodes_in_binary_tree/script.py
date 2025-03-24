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
    def __init__(self) -> None:
        self.count = 0

    def backtrack(self, node: TreeNode | None, max_so_far: int) -> None:
        if not node:
            return

        # If current node >= max seen so far, count it
        if node.val >= max_so_far:
            self.count += 1
            max_so_far = node.val  # Update max

        # Traverse left and right
        self.backtrack(node.left, max_so_far)
        self.backtrack(node.right, max_so_far)

    def goodNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        self.backtrack(root, root.val)
        return self.count
