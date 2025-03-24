# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        values: set[ListNode] = set()
        curr = head

        while curr:
            if curr in values:
                return True
            else:
                values.add(curr)
                curr = curr.next

        return False
