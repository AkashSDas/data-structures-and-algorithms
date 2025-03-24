import pytest

from src.problems.linked_list.linked_list_cycle.script import (  # Adjust import path accordingly
    ListNode,
    Solution,
)


def list_to_linkedlist_with_cycle(items: list[int], pos: int) -> ListNode | None:
    """Helper function to convert list to linked list and create a cycle."""

    if not items:
        return None

    head = ListNode(items[0])
    current = head
    nodes = [head]

    for item in items[1:]:
        new_node = ListNode(item)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
        print("HERE")

    if pos != -1:
        if 0 <= pos < len(nodes):
            current.next = nodes[pos]
        else:
            raise ValueError(f"Invalid pos: {pos}")

    return head


@pytest.mark.parametrize(
    "items, pos, expected_output",
    [
        ([3, 2, 0, -4], 1, True),  # cycle at index 1
        ([1, 2], 0, True),  # cycle at index 0
        ([1], -1, False),  # single node, no cycle
        ([1, 2, 3, 4, 5], -1, False),  # no cycle
        ([], -1, False),  # empty list
        ([1, 2, 3, 4], 2, True),  # cycle at index 2
    ],
)
def test_has_cycle(items, pos, expected_output):
    solution = Solution()
    head = list_to_linkedlist_with_cycle(items, pos)
    assert solution.hasCycle(head) == expected_output
