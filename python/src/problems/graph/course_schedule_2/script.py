from typing import List
from collections import defaultdict, deque


# Solution Implementation
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        prereq_count = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            prereq_count[dest] += 1

        queue = deque([i for i in range(numCourses) if prereq_count[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                prereq_count[neighbor] -= 1
                if prereq_count[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []
