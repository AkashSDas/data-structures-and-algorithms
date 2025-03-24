import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start = 1
        end = max(piles)
        result = end

        while start <= end:
            mid = start + (end - start) // 2

            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / mid)

            if h >= hrs:
                result = mid
                end = mid - 1
            else:
                start = mid + 1

        return result
