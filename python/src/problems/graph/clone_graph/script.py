from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: list["Node"] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if not node:
            return None

        old_to_new = {}

        def dfs(n: Node) -> Node:
            if n in old_to_new:
                return old_to_new[n]

            copy = Node(n.val)
            old_to_new[n] = copy

            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)

    def cloneGraph2(self, node: Node | None) -> Node | None:
        if not node:
            return

        old_new_mapping: dict[Node, Node] = {}
        queue: deque[Node] = deque([node])

        # Clone the first node
        old_new_mapping[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            # Go through each neighbor
            for neighbor in curr.neighbors:
                if neighbor not in old_new_mapping:
                    # Clone neighbor and add to queue
                    old_new_mapping[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Link cloned node to cloned neighbor
                old_new_mapping[curr].neighbors.append(old_new_mapping[neighbor])

        return old_new_mapping[node]
