class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = [0] * 26
        t_counts = [0] * 26

        for char in s:
            idx = ord(char) - 97
            s_counts[idx] += 1

        for char in t:
            idx = ord(char) - 97
            t_counts[idx] += 1

        for idx in range(0, len(s_counts)):
            if s_counts[idx] != t_counts[idx]:
                return False

        return True
