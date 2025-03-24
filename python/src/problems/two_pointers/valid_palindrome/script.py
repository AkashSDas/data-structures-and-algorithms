import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = self.clean_up(s)

        for start_idx in range(len(v)):
            end_idx = len(v) - start_idx - 1

            if v[start_idx] != v[end_idx]:
                return False

        return True

    def clean_up(self, s: str) -> str:
        v = "".join([c.strip() for c in s.split(" ")])
        v = [c for c in v]
        v = filter(lambda x: x != "", v)
        v = map(lambda x: x.lower(), v)
        v = filter(lambda x: x in string.ascii_lowercase or x in string.digits, v)

        return "".join(v)
