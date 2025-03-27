class Solution:
    def __init__(self) -> None:
        self.longest = ""

    def is_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def longestPalindrome1(self, s: str) -> str:
        visited: set[int] = set()

        def dfs(idx: int, sub_str: str) -> None:
            if idx >= len(s):
                return

            visited.add(idx)

            curr_str = sub_str + s[idx]
            if len(curr_str) > len(self.longest) and self.is_palindrome(curr_str):
                self.longest = curr_str

            if idx + 1 not in visited:
                dfs(idx + 1, "")

            dfs(idx + 1, curr_str)

        dfs(0, "")
        return self.longest

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, max_len = 0, 0

        def expand_around_center(left: int, right: int):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > max_len:
                    start, max_len = left, curr_len
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_around_center(i, i)  # Odd-length palindrome
            expand_around_center(i, i + 1)  # Even-length palindrome

        return s[start : start + max_len]
