class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        nums.sort()

        def dfs(idx: int, curr: list[int], available: list[int]) -> None:
            if not available:
                result.append(curr.copy())
                return

            if idx >= len(nums):
                return

            curr.append(nums[idx])
            new_idx = idx + 1

            if new_idx == len(nums):
                dfs(new_idx, curr, available=[])
                curr.pop()
                dfs(new_idx, curr, available=[])
            else:
                is_same = nums[idx] == nums[new_idx]

                dfs(new_idx, curr, available=nums[new_idx:])
                curr.pop()

                if not is_same:
                    dfs(new_idx, curr, available=nums[new_idx:])
                else:
                    while new_idx < len(nums) and nums[new_idx] == nums[new_idx - 1]:
                        new_idx += 1

                    dfs(new_idx, curr, available=nums[new_idx:])

        dfs(0, [], nums)
        return result
