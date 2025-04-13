class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join([str(digit) for digit in digits]))
        num += 1
        return [int(digit) for digit in str(num)]
