class Solution:
    def back_tracking(
        self,
        max_count: int,
        valid_parentheses: list[str],
        stack: list[str],
        open_count: int,
        close_count: int,
    ) -> None:
        if open_count == close_count and close_count == max_count:
            valid_parentheses.append("".join(stack))
            return

        if open_count < max_count:
            stack.append("(")
            self.back_tracking(
                max_count, valid_parentheses, stack, open_count + 1, close_count
            )
            stack.pop()

        if close_count < open_count:
            stack.append(")")
            self.back_tracking(
                max_count, valid_parentheses, stack, open_count, close_count + 1
            )
            stack.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []

        valid_parentheses: list[str] = []
        stack: list[str] = []

        self.back_tracking(n, valid_parentheses, stack, 0, 0)

        return valid_parentheses
