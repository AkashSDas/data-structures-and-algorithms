import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-w for w in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            w1 = -heapq.heappop(max_heap)
            w2 = -heapq.heappop(max_heap)
            result = max(w1, w2) - min(w1, w2)
            print(f"{w1=}, {w2=}, {result=}")

            if result != 0:
                heapq.heappush(max_heap, -result)

        if max_heap:
            return -heapq.heappop(max_heap)
        else:
            return 0
