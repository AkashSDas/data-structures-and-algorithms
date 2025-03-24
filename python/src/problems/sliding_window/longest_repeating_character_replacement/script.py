class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts: dict[str, int] = {}
        max_len = 0
        left = 0
        max_frequency = 0

        for right in range(0, len(s)):
            if char_counts.get(s[right]) is None:
                char_counts[s[right]] = 1
            else:
                char_counts[s[right]] += 1

            max_frequency = max(max_frequency, char_counts[s[right]])

            while (right - left + 1 - max_frequency) > k:
                char_counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
