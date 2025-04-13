class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize cache with proper dimensions
        cache = [
            [float("inf") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]

        # Base case: fill last row and column
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # Bottom-up dynamic programming
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i][j + 1],  # Insert
                        cache[i + 1][j],  # Delete
                        cache[i + 1][j + 1],  # Replace
                    )

        return int(cache[0][0])
