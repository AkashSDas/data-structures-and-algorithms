class Solution:
    def __init__(self) -> None:
        self.max_length = 0

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        def get_indexes(char: str, text: str) -> list[int]:
            result: list[int] = []

            for idx, c in enumerate(text):
                if c == char:
                    result.append(idx)

            return result

        def match(char1_idx: int, char2_idx: int) -> None:
            curr_length = 1

            if char1_idx == len(text1) - 1:
                if curr_length > self.max_length:
                    self.max_length = curr_length
                return

            for char1_next in text1[char1_idx + 1 :]:
                char2_next_idxs = get_indexes(char1_next, text2[char2_idx + 1 :])

                if not char2_next_idxs:
                    continue
                else:
                    char2_next_idx = char2_next_idxs[0]
                    char2_idx = char2_next_idx
                    curr_length += 1

            if curr_length > self.max_length:
                self.max_length = curr_length

        for char1_idx, char1 in enumerate(text1):
            indexes = get_indexes(char1, text2)

            if not indexes:
                continue
            else:
                for char2_idx in indexes:
                    match(char1_idx, char2_idx)

        return self.max_length
