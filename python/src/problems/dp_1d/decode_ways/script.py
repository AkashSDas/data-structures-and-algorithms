class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(idx: int) -> int:
            if idx in dp:
                return dp[idx]
            if s[idx] == "0":
                return 0

            res = dfs(idx + 1)

            in_bound = idx + 1 < len(s)
            start_with_one = s[idx] == "1"
            start_with_two = s[idx] == "2"
            if in_bound and (
                start_with_one or (start_with_two and s[idx + 1] in "0123456")  # max 26
            ):
                res += dfs(idx + 2)

            dp[idx] = res
            return res

        return dfs(0)
