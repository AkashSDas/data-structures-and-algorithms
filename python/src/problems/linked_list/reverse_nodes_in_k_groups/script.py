# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def reverse_group(self, start: ListNode, end: ListNode, count: int) -> None:
        curr_count = 0
        curr = start
        prev_node: ListNode | None = None
        final_next_node = end.next

        while curr_count < count:
            assert curr is not None

            next_node = curr.next

            curr.next = prev_node  # Reverse pointer
            prev_node = curr
            curr = next_node
            curr_count += 1

        # Connect tail (start) to the next part
        start.next = final_next_node

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        count = 0
        curr = head
        last_start = head
        last_end: ListNode | None = None
        final_head: ListNode | None = None

        while curr and last_start:
            if count + 1 == k:
                next_node = curr.next

                self.reverse_group(
                    start=last_start,
                    end=curr,
                    count=k,
                )

                if not final_head:
                    final_head = curr  # First reversed group becomes head

                if last_end:
                    last_end.next = curr  # Connect previous group to current

                last_end = last_start
                last_start = next_node
                curr = next_node
                count = 0
            else:
                count += 1
                curr = curr.next

        return final_head if final_head else head
