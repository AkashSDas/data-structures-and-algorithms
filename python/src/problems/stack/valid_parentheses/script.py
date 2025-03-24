class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        stack: list[str] = []

        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                last_opening_bracket = stack.pop()
                if last_opening_bracket != brackets[char]:
                    return False

        if len(stack) != 0:
            return False

        return True
