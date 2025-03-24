from typing import Self


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: "Node | None" = None


class Queue:
    def __init__(self) -> None:
        self.size = 0
        self.head: "Node | None" = None
        self.curr: "Node | None" = None

    def enqueue(self, val: int) -> None:
        node = Node(val)
        self.size += 1

        if not self.head:
            self.head = node
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = node

    def dequeue(self) -> Node | None:
        if not self.head:
            return None
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node

    def peek(self) -> Node | None:
        return self.head

    def find(self, val: int) -> Node | None:
        if self.head:
            curr = self.head

            while curr:
                if curr.val == val:
                    return curr
                else:
                    curr = curr.next

        return None

    def to_list(self) -> list[int]:
        result: list[int] = []

        if self.head:
            curr = self.head

            while curr:
                result.append(curr.val)
                curr = curr.next

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

    def __len__(self) -> int:
        return self.size
