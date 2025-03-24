from typing import Literal


class PriorityQueue:
    LEFT: Literal[-1] = -1
    RIGHT: Literal[1] = 1

    def __init__(self) -> None:
        # This is a min heap variant where parent is smaller than the child
        self.heap: list[int] = []

    def __str__(self) -> str:
        return str(self.heap)

    def __len__(self) -> int:
        return len(self.heap)

    def peek(self) -> int | None:
        if len(self) > 0:
            return self.heap[0]
        else:
            return None

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.bubble_up(value)

    def remove(self, value: int) -> None:
        while True:
            idxs = self.get_indexes(value)
            if not idxs:
                return

            idx = idxs[-1]  # Always get the latest index
            self.heap[idx] = self.heap[-1]  # Replace with the last element
            self.heap.pop()  # Remove the last element

            if len(self) == 0:
                return

            if idx >= len(self):
                # Last element was removed, no need to bubble
                continue

            parent_idx = self.get_parent_index(idx)

            if parent_idx == -1:
                self.bubble_down(idx)
            else:
                if self.heap[parent_idx] > self.heap[idx]:
                    self.bubble_up(idx)
                else:
                    self.bubble_down(idx)

    def bubble_down(self, idx: int) -> None:
        while True:
            swap_with = self.get_swap_with_child_index(idx)
            child_idx = swap_with[1]

            if child_idx is None:
                break
            else:
                if self.heap[idx] > self.heap[child_idx]:
                    tmp = self.heap[idx]
                    self.heap[idx] = self.heap[child_idx]
                    self.heap[child_idx] = tmp
                    idx = child_idx
                else:
                    break

    def get_swap_with_child_index(self, parent_idx: int) -> list[int | None]:
        left_idx, right_idx = self.get_child_indexes(parent_idx)

        if not left_idx and not right_idx:
            return [None, None]
        elif left_idx is None:
            return [self.RIGHT, right_idx]
        elif right_idx is None:
            return [self.LEFT, left_idx]
        else:
            if self.heap[left_idx] < self.heap[right_idx]:
                return [self.LEFT, left_idx]
            else:
                return [self.RIGHT, right_idx]

    def get_child_indexes(self, parent_idx: int) -> tuple[int | None, int | None]:
        right_idx: int | None = parent_idx * 2 + 2
        left_idx: int | None = parent_idx * 2 + 1

        if right_idx >= len(self):
            right_idx = None

        if left_idx >= len(self):
            left_idx = None

        return left_idx, right_idx

    def bubble_up(self, value: int) -> None:
        while True:
            idxs = self.get_indexes(value)

            # Value doesn't exists in the PQ
            if not idxs:
                break

            idx = idxs[-1]  # Last is the latest index for the value
            parent_idx = self.get_parent_index(idx)

            if parent_idx == -1:
                break

            if self.heap[parent_idx] > self.heap[idx]:
                # Min heap property is violated, swap parent and child
                tmp = self.heap[parent_idx]
                self.heap[parent_idx] = self.heap[idx]
                self.heap[idx] = tmp
            else:
                break

    def get_indexes(self, value: int) -> list[int]:
        idxs: list[int] = []

        for idx, v in enumerate(self.heap):
            if v == value:
                idxs.append(idx)

        return idxs

    def get_parent_index(self, child_index: int) -> int:
        # Root node
        if child_index == 0:
            return -1

        # Why this formula for calculating parent index?
        # https://cs.stackexchange.com/questions/130167/why-does-the-formula-floori-1-2-find-the-parent-node-in-a-binary-heap
        return (child_index - 1) // 2
