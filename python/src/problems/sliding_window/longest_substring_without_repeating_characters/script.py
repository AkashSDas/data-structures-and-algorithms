class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr: set[str] = set()
        max_len = 0
        left = 0

        for right in range(0, len(s)):
            while s[right] in substr:
                substr.remove(s[left])
                left += 1

            substr.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
