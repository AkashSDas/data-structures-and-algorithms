from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        prereq_count = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            prereq_count[course] += 1

        queue = deque([i for i, count in enumerate(prereq_count) if count == 0])
        finished = 0

        while queue:
            course = queue.popleft()
            finished += 1

            for next_course in graph[course]:
                prereq_count[next_course] -= 1

                if prereq_count[next_course] == 0:
                    queue.append(next_course)

        return finished == numCourses
