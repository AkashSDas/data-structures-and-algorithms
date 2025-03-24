class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value

        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}

        self.least_used = Node(0, 0)
        self.most_used = Node(0, 0)

        self.least_used.next = self.most_used
        self.most_used.prev = self.least_used

    def get_most_used(self) -> Node | None:
        return self.most_used.prev

    def get_least_used(self) -> Node | None:
        return self.least_used.prev

    def remove(self, node: Node) -> None:
        """Remove node from doubly linked list"""

        prev_node = node.prev
        next_node = node.next

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

    def insert(self, node: Node) -> None:
        """Insert node at the right end i.e. the most used"""

        prev_node = self.most_used.prev

        if prev_node:
            prev_node.next = node
            node.prev = prev_node

        node.next = self.most_used
        self.most_used.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove the least recently used value
            lru = self.least_used.next

            if lru:
                self.remove(lru)
                del self.cache[lru.key]
