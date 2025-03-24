from typing import List, Optional

import pytest

from src.problems.linked_list.merge_two_sorted_lists.script import ListNode, Solution


def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    """Helper function to convert list to linked list."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert linked list to list."""
    items = []
    while head:
        items.append(head.val)
        head = head.next
    return items


@pytest.mark.parametrize(
    "list1, list2, expected_output",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),  # both lists empty
        ([], [0], [0]),  # first list empty
        ([5], [], [5]),  # second list empty
        ([2, 5, 7], [1, 3, 6], [1, 2, 3, 5, 6, 7]),
        ([1, 1, 2], [1, 1, 2], [1, 1, 1, 1, 2, 2]),
        ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
    ],
)
def test_merge_two_lists(list1, list2, expected_output):
    solution = Solution()
    l1 = list_to_linkedlist(list1)
    l2 = list_to_linkedlist(list2)
    merged_head = solution.mergeTwoLists(l1, l2)
    assert linkedlist_to_list(merged_head) == expected_output
