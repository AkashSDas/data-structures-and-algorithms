# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None,
    ) -> ListNode | None:
        node: ListNode | None = None
        head_node: ListNode | None = None
        carry_forward: int | None = 0

        curr1 = l1
        curr2 = l2

        while curr1 or curr2:

            new_node: ListNode | None = None

            if curr1 and curr2:

                add_value = curr1.val + curr2.val
                if carry_forward:
                    add_value += carry_forward
                    carry_forward = None
                add_value_str = str(add_value)

                if len(add_value_str) > 1:
                    carry_forward = int(add_value_str[0])
                    new_node = ListNode(val=int(add_value_str[1]))
                else:
                    new_node = ListNode(val=int(add_value_str))

                curr1 = curr1.next
                curr2 = curr2.next

            elif curr1:
                add_value = curr1.val
                if carry_forward:
                    add_value += carry_forward
                    carry_forward = None
                add_value_str = str(add_value)

                if len(add_value_str) > 1:
                    carry_forward = int(add_value_str[0])
                    new_node = ListNode(val=int(add_value_str[1]))
                else:
                    new_node = ListNode(val=int(add_value_str))

                curr1 = curr1.next

            elif curr2:
                add_value = curr2.val
                if carry_forward:
                    add_value += carry_forward
                    carry_forward = None
                add_value_str = str(add_value)

                if len(add_value_str) > 1:
                    carry_forward = int(add_value_str[0])
                    new_node = ListNode(val=int(add_value_str[1]))
                else:
                    new_node = ListNode(val=int(add_value_str))

                curr2 = curr2.next

            if new_node:
                if not head_node:
                    head_node = new_node

                if not node:
                    node = new_node
                else:
                    node.next = new_node
                    node = new_node

        if carry_forward:
            new_node = ListNode(val=int(carry_forward))

            if node:
                node.next = new_node

        return head_node
