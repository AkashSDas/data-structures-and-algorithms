class MinStack:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []
        self.min: None | int = None

    def push(self, val: int) -> None:
        if self.min is None or self.min > val:
            self.min = val

        self.stack.append((val, self.min))

    def pop(self) -> None:
        result = self.stack.pop()

        if self.min == result[1]:
            if len(self.stack) > 0:
                self.min = self.stack[-1][1]
            else:
                self.min = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        assert type(self.min) == int
        return self.min
