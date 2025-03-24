class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache: dict[int, int] = {}  # num:idx

        for idx, num in enumerate(nums):
            diff = target - num

            if cache.get(diff) is not None:
                return [cache[diff], idx]
            else:
                cache[num] = idx

        return [-1, -1]
