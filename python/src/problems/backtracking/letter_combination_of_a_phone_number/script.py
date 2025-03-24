class Solution:
    def __init__(self) -> None:
        self.digits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits: str) -> list[str]:
        result: list[str] = []

        def backtrack(idx: int, curr: list[str]) -> None:
            if idx >= len(digits):
                if curr:
                    result.append("".join(curr))
                return

            digit = digits[idx]
            options = self.digits[digit]

            for opt in options:
                curr.append(opt)
                backtrack(idx + 1, curr.copy())
                curr.pop()

        backtrack(0, [])
        return result
