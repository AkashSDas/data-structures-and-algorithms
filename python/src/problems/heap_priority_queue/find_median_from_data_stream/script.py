import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap for the smaller half
        self.large = []  # Min-heap for the larger half

    def addNum(self, num: int) -> None:
        # Add to max heap (invert sign for max behavior)
        heapq.heappush(self.small, -num)

        # Balance: Move the largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Maintain size property
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


class MedianFinder2:
    def __init__(self):
        self.vals: list[int] = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.vals, num)

    def findMedian(self) -> float:
        if len(self.vals) % 2 == 0:
            mid1 = len(self.vals) // 2

            add_back: list[int] = []
            for _ in range(mid1 - 1):
                add_back.append(heapq.heappop(self.vals))

            v1 = heapq.heappop(self.vals)
            v2 = heapq.heappop(self.vals)

            for val in [*add_back, v1, v2]:
                heapq.heappush(self.vals, val)

            return (v1 + v2) / 2
        else:
            mid = len(self.vals) // 2

            add_back: list[int] = []
            for _ in range(mid):
                add_back.append(heapq.heappop(self.vals))

            v = heapq.heappop(self.vals)

            for val in [*add_back, v]:
                heapq.heappush(self.vals, val)

            return v


class MedianFinder3:
    def __init__(self):
        self.vals: list[int] = []

    def addNum(self, num: int) -> None:
        self.vals.append(num)
        self.vals.sort()

    def findMedian(self) -> float:
        if len(self.vals) % 2 == 0:
            mid1 = len(self.vals) // 2
            mid2 = (len(self.vals) // 2) - 1
            return (self.vals[mid1] + self.vals[mid2]) / 2
        else:
            mid = len(self.vals) // 2
            return self.vals[mid]
