from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = Counter(s1)
        window_counts = Counter(s2[: len(s1)])

        if s1_counts == window_counts:
            return True

        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            end_char = s2[i]

            # Add new character
            window_counts[end_char] += 1

            # Remove old character
            window_counts[start_char] -= 1
            if window_counts[start_char] == 0:
                del window_counts[start_char]

            if window_counts == s1_counts:
                return True

        return False
