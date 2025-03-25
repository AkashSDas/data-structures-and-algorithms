class Solution:
    def checkValidString(self, s: str) -> bool:
        # Maximum and minimum opening parenthesis
        left_max, left_min = 0, 0

        for char in s:
            if char == "(":
                left_max += 1
                left_min += 1
            elif char == ")":
                left_max -= 1
                left_min -= 1
            else:
                left_min -= 1
                left_max += 1

            if left_max < 0:
                return False

            if left_min < 0:  # s = "( * ) ("
                left_min = 0

        return left_min == 0
