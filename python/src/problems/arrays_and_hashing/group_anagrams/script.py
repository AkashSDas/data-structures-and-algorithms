class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[str, list[str]] = {}

        for word in strs:
            counts = [0] * 26

            for char in word:
                idx = ord(char) - 97
                counts[idx] += 1

            key = str(counts)

            if groups.get(key):
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
