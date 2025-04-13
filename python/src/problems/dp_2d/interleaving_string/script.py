class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # Matrix: len(s1) x len(s2)
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for idx1 in range(len(s1), -1, -1):
            for idx2 in range(len(s2), -1, -1):
                idx3 = idx1 + idx2

                if idx1 < len(s1) and s1[idx1] == s3[idx3] and dp[idx1 + 1][idx2]:
                    dp[idx1][idx2] = True

                if idx2 < len(s2) and s2[idx2] == s3[idx3] and dp[idx1][idx2 + 1]:
                    dp[idx1][idx2] = True

        return dp[0][0]

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        cache: dict[tuple[int, int], bool] = {}

        def dfs(idx1: int, idx2: int) -> bool:
            if idx1 == len(s1) and idx2 == len(s2):
                return True
            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]

            idx3 = idx1 + idx2

            if idx1 < len(s1) and s1[idx1] == s3[idx3] and dfs(idx1 + 1, idx2):
                return True

            if idx2 < len(s2) and s2[idx2] == s3[idx3] and dfs(idx1, idx2 + 1):
                return True

            cache[(idx1, idx2)] = False
            return False

        return dfs(0, 0)
