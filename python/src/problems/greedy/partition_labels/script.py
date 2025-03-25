class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        indexes: dict[str, int] = {char: idx for idx, char in enumerate(s)}

        start = 0
        end = indexes[s[start]]

        result: list[int] = []
        curr = 0

        while start < len(s):
            char = s[start]
            curr += 1

            if indexes[char] > end:
                end = indexes[char]

            if start == end:
                result.append(curr)
                curr = 0

                if end + 1 < len(s) - 1:
                    end = indexes[s[start + 1]]

            start += 1

        return result
