import pytest

from src.problems.linked_list.add_two_numbers.script import ListNode, Solution


# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# Helper function to convert linked list to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Pytest test cases
@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # 342 + 465 = 807
        ([0], [0], [0]),  # 0 + 0 = 0
        (
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
        ),  # Big numbers with carry
        ([1], [9, 9, 9], [0, 0, 0, 1]),  # Carry over to new digit
        ([5], [5], [0, 1]),  # Simple carry (5+5=10)
        ([2, 4], [5, 6, 7], [7, 0, 8]),  # Unequal lengths
    ],
)
def test_addTwoNumbers(l1, l2, expected):
    sol = Solution()
    l1_list = list_to_linkedlist(l1)
    l2_list = list_to_linkedlist(l2)
    result = sol.addTwoNumbers(l1_list, l2_list)
    assert linkedlist_to_list(result) == expected
