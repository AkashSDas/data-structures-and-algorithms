class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result: list[int] = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []

        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                last_day = stack.pop()
                result[last_day[1]] = idx - last_day[1]

            stack.append((temp, idx))

        return result

    def dailyTemperatures2(self, temperatures: list[int]) -> list[int]:
        result: list[int] = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []

        for idx, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temp, idx))
            else:
                new_stack: list[tuple[int, int]] = []

                for item in stack:
                    if item[0] < temp:
                        result[item[1]] = idx - item[1]
                    else:
                        new_stack.append(item)

                new_stack.append((temp, idx))
                stack = new_stack

        return result
