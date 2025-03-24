from typing import TypedDict


# Definition for a Node.
class Node:
    def __init__(
        self,
        x: int,
        next: "Node | None" = None,
        random: "Node | None" = None,
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class OriginalNodeInfo(TypedDict):
    old_node: Node


class NewNodeInfo(TypedDict):
    new_node: Node


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        curr_node = head
        old_mapping: dict[Node, OriginalNodeInfo] = {}

        while curr_node:
            old_mapping[curr_node] = {
                "old_node": curr_node,
            }

            curr_node = curr_node.next

        new_mapping: dict[Node, NewNodeInfo] = {}
        prev_node: Node | None = None
        curr_node = head

        while curr_node:
            new_node_info = new_mapping.get(curr_node)
            old_node_info = old_mapping[curr_node]
            old_node = old_node_info["old_node"]

            if not new_node_info:
                new_node = Node(
                    x=curr_node.val,
                    next=None,
                    random=None,
                )

                new_mapping[curr_node] = {"new_node": new_node}

            curr_new_node = new_mapping[curr_node]["new_node"]

            if old_node.random:
                random_node_info = new_mapping.get(old_node.random)

                if not random_node_info:
                    random_new_node = Node(
                        x=old_node.random.val,
                        next=None,
                        random=None,
                    )

                    new_mapping[old_node.random] = {"new_node": random_new_node}

                random_new_node = new_mapping[old_node.random]["new_node"]
                curr_new_node.random = random_new_node

            if prev_node:
                prev_new_node = new_mapping[prev_node]["new_node"]
                prev_new_node.next = curr_new_node

            prev_node = curr_node
            curr_node = curr_node.next

        if not head:
            return None

        return new_mapping.get(head, {}).get("new_node")
