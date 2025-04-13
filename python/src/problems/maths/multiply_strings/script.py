class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for idx1 in range(len(num1)):
            for idx2 in range(len(num2)):
                digit = int(num1[idx1]) * int(num2[idx2])

                result[idx1 + idx2] += digit
                result[idx1 + idx2 + 1] += result[idx1 + idx2] // 10
                result[idx1 + idx2] = result[idx1 + idx2] % 10

        result, start = result[::-1], 0
        while start < len(result) and result[start] == 0:
            start += 1

        return "".join(map(str, result[start:]))
