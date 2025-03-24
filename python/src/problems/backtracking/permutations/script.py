class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(curr: list[int], remaining: list[int]) -> None:
            if not remaining:
                result.append(curr[:])  # or curr.copy()
                return

            for i in range(len(remaining)):
                next_num = remaining[i]
                # Choose next_num and remove it from remaining
                backtrack(curr + [next_num], remaining[:i] + remaining[i + 1 :])

        backtrack([], nums)
        return result
