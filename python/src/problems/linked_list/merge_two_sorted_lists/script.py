# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        prev_node: ListNode | None = None
        head_node: ListNode | None = None
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                if not prev_node:
                    prev_node = curr1
                    head_node = prev_node
                else:
                    prev_node.next = curr1
                    prev_node = curr1

                curr1 = curr1.next
            else:
                if not prev_node:
                    prev_node = curr2
                    head_node = prev_node
                else:
                    prev_node.next = curr2
                    prev_node = curr2

                curr2 = curr2.next

        while curr1:
            if not prev_node:
                prev_node = curr1
                head_node = prev_node
            else:
                prev_node.next = curr1
                prev_node = curr1

            curr1 = curr1.next

        while curr2:
            if not prev_node:
                prev_node = curr2
                head_node = prev_node
            else:
                prev_node.next = curr2
                prev_node = curr2

            curr2 = curr2.next

        return head_node
