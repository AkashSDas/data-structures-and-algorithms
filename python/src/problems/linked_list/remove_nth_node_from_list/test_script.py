from src.problems.linked_list.remove_nth_node_from_list.script import ListNode, Solution


def list_to_linkedlist(items: list[int]) -> ListNode | None:
    """Helper: Convert list to linked list."""

    if not items:
        return None

    head = ListNode(items[0])
    current = head

    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next

    return head


def linkedlist_to_list(head: ListNode | None) -> list[int]:
    """Helper: Convert linked list back to list."""

    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def test_remove_nth_from_end_case1():
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    n = 2
    result = Solution().removeNthFromEnd(head, n)
    assert linkedlist_to_list(result) == [1, 2, 3, 5]


def test_remove_nth_from_end_case2():
    head = list_to_linkedlist([1])
    n = 1
    result = Solution().removeNthFromEnd(head, n)
    assert linkedlist_to_list(result) == []


def test_remove_nth_from_end_case3():
    head = list_to_linkedlist([1, 2])
    n = 1
    result = Solution().removeNthFromEnd(head, n)
    assert linkedlist_to_list(result) == [1]


def test_remove_nth_from_end_case4():
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    n = 5
    result = Solution().removeNthFromEnd(head, n)
    assert linkedlist_to_list(result) == [2, 3, 4, 5]


def test_remove_nth_from_end_case5():
    head = list_to_linkedlist([1, 2, 3])
    n = 3
    result = Solution().removeNthFromEnd(head, n)
    assert linkedlist_to_list(result) == [2, 3]
