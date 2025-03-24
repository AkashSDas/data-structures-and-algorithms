from collections import deque
import heapq
from typing import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-count for count in count.values()]
        heapq.heapify(max_heap)

        time = 0
        queue: deque[tuple[int, int]] = deque()  # (-count, idle time)

        while max_heap or queue:
            time += 1

            if not max_heap:
                time = queue[0][1]  # skipping to the interval from which we process
            else:
                # removing 1 from tasks and task is negative, so +1
                count = 1 + heapq.heappop(max_heap)

                if count:
                    queue.append((count, time + n))  # available after time + n

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time
