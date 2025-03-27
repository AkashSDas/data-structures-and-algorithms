class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        combinations: list[str] = []

        def expand_around_center(left: int, right: int):
            nonlocal combinations
            while left >= 0 and right < len(s) and s[left] == s[right]:
                combinations.append(s[left : right + 1])

                left -= 1
                right += 1

        for i in range(len(s)):
            expand_around_center(i, i)  # Odd-length palindrome
            expand_around_center(i, i + 1)  # Even-length palindrome

        return len(combinations)
