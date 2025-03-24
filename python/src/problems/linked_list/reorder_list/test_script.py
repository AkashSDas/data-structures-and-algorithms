import pytest

from src.problems.linked_list.reorder_list.script import ListNode, Solution


def list_to_linkedlist(items: list[int]) -> ListNode | None:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linkedlist_to_list(head: ListNode | None) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([], []),
        ([10, 20, 30, 40, 50, 60], [10, 60, 20, 50, 30, 40]),
    ],
)
def test_reorder_list(input_list, expected_output):
    head = list_to_linkedlist(input_list)
    Solution().reorderList(head)
    output = linkedlist_to_list(head)
    assert output == expected_output
