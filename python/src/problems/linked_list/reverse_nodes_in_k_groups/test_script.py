import pytest

from src.problems.linked_list.reverse_nodes_in_k_groups.script import ListNode, Solution


def list_to_linkedlist(arr):
    head = ListNode(0)
    curr = head
    for num in arr:
        print("Hiiabbbbaa")
        curr.next = ListNode(num)
        curr = curr.next
    return head.next


def linkedlist_to_list(head):
    arr = []
    while head:
        print("Hiiaaa")
        arr.append(head.val)
        head = head.next
    return arr


@pytest.mark.parametrize(
    "input_list, k, expected",
    [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
        ([1], 1, [1]),
        ([1, 2], 3, [1, 2]),  # Less than k nodes, no change
        ([], 2, []),  # Empty list
    ],
)
def test_reverseKGroup(input_list, k, expected):
    head = list_to_linkedlist(input_list)
    result = Solution().reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected
