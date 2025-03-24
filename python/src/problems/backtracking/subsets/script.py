class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        subset: list[int] = []

        def dfs(idx: int) -> None:
            if idx >= len(nums):
                result.append(subset.copy())
            else:
                subset.append(nums[idx])
                dfs(idx + 1)

                subset.pop()
                dfs(idx + 1)

        dfs(0)
        return result
