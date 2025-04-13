class Solution:
    def square_each_place(self, num: int) -> int:
        digits = [d for d in str(num)]
        return sum([int(digit) ** 2 for digit in digits])

    def isHappy(self, n: int) -> bool:
        curr = n
        visited: set[int] = {curr}

        while curr != 1:
            curr = self.square_each_place(curr)

            if curr in visited:
                return False
            else:
                visited.add(curr)

        return True
