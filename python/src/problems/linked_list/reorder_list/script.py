# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return

        items: list[ListNode] = []
        curr = head
        while curr:
            items.append(curr)
            curr = curr.next

        is_even = len(items) % 2 == 0

        if is_even:
            max_idx = (len(items) // 2) - 1
        else:
            max_idx = len(items) // 2

        for idx in range(len(items)):
            node = items[idx]

            if idx == max_idx:
                if is_even and node.next:
                    node.next.next = None
                else:
                    node.next = None

                break
            else:
                add_node = items[len(items) - 1 - idx]

                next_node = node.next
                node.next = add_node
                add_node.next = next_node
