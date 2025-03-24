class Solution:
    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def partition(self, s: str) -> list[list[str]]:
        result: list[list[str]] = []
        curr_partition: list[str] = []

        def dfs(idx: int) -> None:
            if idx >= len(s):
                result.append(curr_partition.copy())
                return

            for i in range(idx, len(s)):
                if self.is_palindrome(s, idx, i):
                    curr_partition.append(s[idx : i + 1])
                    dfs(i + 1)
                    curr_partition.pop()

        dfs(0)
        return result
