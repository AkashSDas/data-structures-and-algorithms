class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to create linked list from Python list
    @staticmethod
    def from_list(values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper method to convert linked list to Python list
    @staticmethod
    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


class Solution:
    def get_min_node(self, lists: list[ListNode]) -> tuple[ListNode, int]:
        min_node: ListNode | None = None
        idx = -1

        for i, node in enumerate(lists):
            if not min_node or node.val < min_node.val:
                min_node = node
                idx = i

        assert min_node is not None
        assert idx != -1

        return min_node, idx

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        curr_pointers: list[ListNode] = []

        for list_head_node in lists:
            if list_head_node:
                curr_pointers.append(list_head_node)

        head_node: ListNode | None = None
        prev_node: ListNode | None = None

        while len(curr_pointers) > 0:
            min_node, idx = self.get_min_node(curr_pointers)

            if min_node.next:
                curr_pointers[idx] = min_node.next
            else:
                curr_pointers.pop(idx)

            if not prev_node:
                head_node = min_node
            else:
                prev_node.next = min_node

            prev_node = min_node

        if prev_node:
            prev_node.next = None

        return head_node
