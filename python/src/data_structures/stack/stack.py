from typing import Self


class Node:
    def __init__(self, val: int, next: "Node | None") -> None:
        self.val = val
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.head: Node | None = None
        self.curr: Node | None = None

    def push(self, val: int) -> None:
        node = Node(val, next=self.head)
        self.head = node
        self.size += 1

    def pop(self) -> Node | None:
        if self.head:
            node = self.head
            self.head = node.next
            self.size -= 1
            return node
        else:
            return None

    def peek(self) -> Node | None:
        return self.head

    def find(self, val: int) -> Node | None:
        node = self.head

        while node:
            if node.val == val:
                return node
            else:
                node = node.next

        return None

    def to_list(self) -> list[int]:
        result: list[int] = []
        node = self.head

        while node:
            result.append(node.val)
            node = node.next

        return result

    def __iter__(self) -> Self:
        self.curr = self.head
        return self

    def __next__(self) -> Node:
        if self.curr is None:
            raise StopIteration
        else:
            node = self.curr
            self.curr = self.curr.next
            return node
