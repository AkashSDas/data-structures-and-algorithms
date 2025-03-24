class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        def dfs(idx: int, curr: list[int], total: int) -> None:
            if total == target:
                result.append(curr.copy())
                return

            if idx >= len(candidates) or total > target:
                return

            curr.append(candidates[idx])
            dfs(idx, curr, total + candidates[idx])

            curr.pop()
            dfs(idx + 1, curr, total)

        dfs(0, [], 0)

        return result

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []

        def solve(nums: list[int]) -> None:
            diff = target - sum(nums)

            if diff == 0:
                result.append(nums.copy())
                return
            elif diff > 0:
                valid_nums = list(filter(lambda x: x <= diff, candidates))

                for num in valid_nums:
                    solve([*nums.copy(), num])
            else:
                return

        for num in candidates:
            diff = target - num
            if diff >= 0:
                solve([num])

        unique_result: set[str] = set()
        final_result: list[list[int]] = []

        for vals in result:
            vals.sort()
            vals_str = "_".join([str(n) for n in vals])

            if vals_str not in unique_result:
                unique_result.add(vals_str)
                final_result.append(vals)

        return final_result
