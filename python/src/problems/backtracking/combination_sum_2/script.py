class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        candidates.sort()

        def dfs(idx: int, curr: list[int], total: int) -> None:
            if target == total:
                result.append(curr.copy())
                return

            if idx >= len(candidates) or total > target:
                return

            # Include candidate[idx]
            curr.append(candidates[idx])
            dfs(idx + 1, curr, total + candidates[idx])

            # Exclude candidate[idx]
            curr.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1

            dfs(idx + 1, curr, total)

        dfs(0, [], 0)

        return result
