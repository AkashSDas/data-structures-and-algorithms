from collections import deque


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != (n - 1):  # Should be exactly n-1 edges
            return False

        adjacency_list: list[list[int]] = [[] for _ in range(n)]
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        visited: set[int] = set()
        stack: deque[tuple[int, int]] = deque()  # (node, parent)
        stack.append((0, -1))  # Start from node 0, no parent

        while stack:
            node, parent = stack.pop()
            if node in visited:
                return False  # Cycle detected

            visited.add(node)

            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue  # Don't revisit parent
                else:
                    stack.append((neighbor, node))

        return len(visited) == n  # All nodes must be visited (connected)
