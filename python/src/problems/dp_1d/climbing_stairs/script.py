class Solution:
    def climbStairs(self, n: int) -> int:
        last, second_last = 1, 1

        for _ in range(n - 1):
            tmp = second_last
            second_last = last + second_last
            last = tmp

        return second_last
