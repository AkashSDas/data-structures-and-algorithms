class Solution:
    def get_count(self, v: str) -> dict[str, int]:
        count: dict[str, int] = {}

        for char in v:
            count[char] = count.get(char, 0) + 1

        return count

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_count = self.get_count(t)
        window_count: dict[str, int] = {}

        have = 0
        need = len(t_count)

        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                # Update result if smaller window found
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = [left, right]

                # Shrink window from left
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

        l, r = res

        return s[l : r + 1] if res_len != float("inf") else ""


class Solution1:
    def get_count(self, v: str) -> dict[str, int]:
        count: dict[str, int] = {}

        for char in v:
            if count.get(char) is None:
                count[char] = 1
            else:
                count[char] += 1

        return count

    def includes(self, larger: dict[str, int], smaller: dict[str, int]) -> bool:
        for k1, v1 in smaller.items():
            if larger.get(k1) is not None and larger[k1] >= v1:
                continue
            else:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        substr: None | str = None
        t_count = self.get_count(t)

        for i in range(0, len(s) - len(t) + 1):
            right = i + len(t) - 1

            while right < len(s):
                window = s[i : right + 1]
                w_count = self.get_count(window)

                if self.includes(w_count, t_count):
                    if substr is None or len(window) < len(substr):
                        substr = window
                    else:
                        break
                else:
                    right += 1

        return substr if substr is not None else ""
