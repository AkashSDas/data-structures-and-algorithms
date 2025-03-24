from typing import List, Optional

from src.problems.linked_list.copy_list_with_random_pointer.script import Node, Solution


def list_to_linkedlist_with_random(data: List[List[Optional[int]]]) -> Optional[Node]:
    """Convert [[val, random_index], ...] to linked list with random pointers."""
    if not data:
        return None

    nodes = [Node(val) for val, _ in data]

    # Setting next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Setting random pointers
    for i, (_, rand_idx) in enumerate(data):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]

    return nodes[0]


def linkedlist_to_list_with_random(head: Optional[Node]) -> List[List[Optional[int]]]:
    """Convert linked list with random pointers back to [[val, random_index], ...]."""
    if not head:
        return []

    nodes = []
    index_map = {}

    # First pass: map nodes to indices
    current = head
    idx = 0
    while current:
        index_map[current] = idx
        nodes.append(current)
        current = current.next
        idx += 1

    # Second pass: build result
    result = []
    for node in nodes:
        random_idx = index_map[node.random] if node.random else None
        result.append([node.val, random_idx])

    return result


def test_copy_random_list_example1():
    input_data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = list_to_linkedlist_with_random(input_data)
    copied = Solution().copyRandomList(head)
    output = linkedlist_to_list_with_random(copied)
    assert output == input_data


def test_copy_random_list_example2():
    input_data = [[1, 1], [2, 1]]
    head = list_to_linkedlist_with_random(input_data)
    copied = Solution().copyRandomList(head)
    output = linkedlist_to_list_with_random(copied)
    assert output == input_data


def test_copy_random_list_example3():
    input_data = [[3, None], [3, 0], [3, None]]
    head = list_to_linkedlist_with_random(input_data)
    copied = Solution().copyRandomList(head)
    output = linkedlist_to_list_with_random(copied)
    assert output == input_data


def test_copy_random_list_empty():
    input_data = []
    head = list_to_linkedlist_with_random(input_data)
    copied = Solution().copyRandomList(head)
    output = linkedlist_to_list_with_random(copied)
    assert output == input_data


def test_copy_random_list_single_node():
    input_data = [[42, None]]
    head = list_to_linkedlist_with_random(input_data)
    copied = Solution().copyRandomList(head)
    output = linkedlist_to_list_with_random(copied)
    assert output == input_data
