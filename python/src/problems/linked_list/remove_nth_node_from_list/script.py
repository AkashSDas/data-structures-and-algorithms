# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        mapping: dict[int, ListNode] = {}
        curr = head
        count = 0

        while curr:
            mapping[count] = curr
            curr = curr.next
            count += 1

        rm_idx = len(mapping) - n
        prev_node = mapping.get(rm_idx - 1)
        node = mapping[rm_idx]

        if prev_node:
            prev_node.next = node.next

        del mapping[rm_idx]

        head = mapping.get(0)
        result = head if head else mapping.get(1)
        return result
