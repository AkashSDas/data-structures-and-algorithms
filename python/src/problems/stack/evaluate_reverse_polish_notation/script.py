import math


class Solution:
    def perform_operation(self, lhs: float, rhs: float, operand: str) -> float:
        match operand:
            case "*":
                return lhs * rhs
            case "/":
                result = lhs / rhs
                if result < 0:
                    return math.ceil(result)
                else:
                    return math.floor(result)
            case "-":
                return lhs - rhs
            case "+":
                return lhs + rhs
            case _:
                raise Exception("Invalid operand")

    def evalRPN(self, tokens: list[str]) -> int:
        operands = set(["*", "/", "-", "+"])
        stack: list[float] = []

        for token in tokens:
            if token not in operands:
                stack.append(float(token))
            else:
                rhs = stack.pop()
                lhs = stack.pop()
                result = self.perform_operation(lhs, rhs, token)
                stack.append(result)

        return int(stack[0])
