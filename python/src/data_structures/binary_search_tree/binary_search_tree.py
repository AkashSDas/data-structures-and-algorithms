class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: "Node | None" = None
        self.right: "Node | None" = None


class Tree:
    def __init__(self) -> None:
        self.root: Node | None = None

    # =================================
    # Insert and find
    # =================================

    def insert(self, val: int, parent: Node | None) -> Node:
        if not self.root:
            self.root = Node(val)
            return self.root

        assert parent is not None, "Parent node is needed"

        if val < parent.val:
            if parent.left:
                return self.insert(val, parent.left)
            else:
                parent.left = Node(val)
                return parent.left

        if val > parent.val:
            if parent.right:
                return self.insert(val, parent.right)
            else:
                parent.right = Node(val)
                return parent.right

        raise Exception("Duplicate values are not allowed")

    def find(
        self,
        val: int,
        current: Node | None,
        parent: Node | None = None,
    ) -> tuple[Node | None, Node | None]:
        if not self.root:
            return None, None

        assert current is not None

        if val > current.val:
            if current.right:
                return self.find(val, current.right, current)
            else:
                return None, None
        elif val < current.val:
            if current.left:
                return self.find(val, current.left, current)
            else:
                return None, None
        else:
            return current, parent

    # =================================
    # Delete
    # =================================

    def delete(self, val: int) -> None:
        curr, parent = self.find(val, current=self.root)

        assert curr, "Value doesn't exists in the tree"

        count = self.get_child_count(curr)

        match count:
            case 0:
                self.delete_0_child_node(curr, parent)
            case 1:
                self.delete_1_child_node(curr, parent)
            case 2:
                self.delete_2_child_node(curr)
            case _:
                raise Exception("Invalid binary tree")

    def delete_2_child_node(self, node: Node) -> None:
        # Find the smallest node in the right subtree
        successor = node.right
        successor_parent = node

        assert successor is not None

        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Replace the node to be deleted with the successor
        node.val = successor.val

        # Delete the successor

        successor_child_count = self.get_child_count(successor)
        match successor_child_count:
            case 0:
                self.delete_0_child_node(successor, successor_parent)
            case 1:
                self.delete_1_child_node(successor, successor_parent)
            case _:
                raise Exception("Unreachable scenario")

    def delete_1_child_node(self, node: Node, parent: Node | None) -> None:
        if node == self.root:
            if node.left:
                self.root = node.left
            else:
                self.root = node.right
            return

        assert parent is not None

        if parent.left == node:
            if node.left:
                parent.left = node.left
            else:
                parent.left = node.right

        else:
            if node.right:
                parent.right = node.right
            else:
                parent.right = node.left

    def delete_0_child_node(self, node: Node, parent: Node | None) -> None:
        if node == self.root:
            self.root = None
            return

        assert parent is not None

        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    def get_child_count(self, node: Node) -> int:
        count = 0

        if node.left:
            count += 1
        if node.right:
            count += 1

        return count

    # =================================
    # Traversal
    # =================================

    def traverse_in_order(self) -> list[int]:
        result: list[int] = []
        self.traverse_in_order_helper(self.root, result)
        return result

    def traverse_in_order_helper(self, node: Node | None, result: list[int]) -> None:
        if not node:
            return

        self.traverse_in_order_helper(node.left, result)
        result.append(node.val)
        self.traverse_in_order_helper(node.right, result)

    def traverse_pre_order(self) -> list[int]:
        result: list[int] = []
        self.traverse_pre_order_helper(self.root, result)
        return result

    def traverse_pre_order_helper(self, node: Node | None, result: list[int]) -> None:
        if not node:
            return

        result.append(node.val)
        self.traverse_pre_order_helper(node.left, result)
        self.traverse_pre_order_helper(node.right, result)

    def traverse_post_order(self) -> list[int]:
        result: list[int] = []
        self.traverse_post_order_helper(self.root, result)
        return result

    def traverse_post_order_helper(self, node: Node | None, result: list[int]) -> None:
        if not node:
            return

        self.traverse_post_order_helper(node.left, result)
        self.traverse_post_order_helper(node.right, result)
        result.append(node.val)

    # =================================
    # Invert
    # =================================

    def invert_tree(self) -> None:
        if not self.root:
            return

        queue: list[Node] = [self.root]

        while queue:
            node = queue.pop()

            tmp = node.left
            node.left = node.right
            node.right = tmp

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
