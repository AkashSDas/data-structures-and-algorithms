import pytest

from src.problems.linked_list.reverse_linked_list.script import ListNode, Solution


def list_to_linkedlist(items: list[int]) -> ListNode | None:
    """Helper function to convert list to linked list."""

    if not items:
        return None

    head = ListNode(items[0])
    current = head

    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next

    return head


def linkedlist_to_list(head: ListNode | None) -> list[int]:
    """Helper function to convert linked list to list."""

    items = []

    while head:
        items.append(head.val)
        head = head.next

    return items


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1], [1]),  # single node
        ([], []),  # empty list
        ([1, 2], [2, 1]),  # two nodes
        ([10, 20, 30, 40], [40, 30, 20, 10]),  # even number of nodes
    ],
)
def test_reverse_list(input_list, expected_output):
    solution = Solution()
    head = list_to_linkedlist(input_list)
    reversed_head = solution.reverseList(head)
    assert linkedlist_to_list(reversed_head) == expected_output
