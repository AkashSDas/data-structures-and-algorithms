from src.problems.linked_list.merge_k_sorted_lists.script import ListNode, Solution


def test_example_1():
    lists = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6]),
    ]
    sol = Solution()
    merged = sol.mergeKLists(lists)
    assert ListNode.to_list(merged) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_example_2_empty():
    lists = []
    sol = Solution()
    merged = sol.mergeKLists(lists)
    assert ListNode.to_list(merged) == []


def test_example_3_single_empty_list():
    lists: list[ListNode | None] = [None]
    sol = Solution()
    merged = sol.mergeKLists(lists)
    assert ListNode.to_list(merged) == []


def test_all_empty_lists():
    lists: list[ListNode | None] = [None, None, None]
    sol = Solution()
    merged = sol.mergeKLists(lists)
    assert ListNode.to_list(merged) == []


def test_single_list():
    lists = [ListNode.from_list([1, 2, 3])]
    sol = Solution()
    merged = sol.mergeKLists(lists)
    assert ListNode.to_list(merged) == [1, 2, 3]


def test_lists_with_duplicates():
    lists = [
        ListNode.from_list([1, 3, 3]),
        ListNode.from_list([1, 1, 2]),
        ListNode.from_list([2, 4]),
    ]
    sol = Solution()
    merged = sol.mergeKLists(lists)
    assert ListNode.to_list(merged) == [1, 1, 1, 2, 2, 3, 3, 4]


def test_large_input():
    lists = [ListNode.from_list([i]) for i in range(1000, 0, -1)]
    sol = Solution()
    merged = sol.mergeKLists(lists)
    assert ListNode.to_list(merged) == list(range(1, 1001))
