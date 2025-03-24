class Solution:
    def get_time(self, speed: int, distance: int) -> float:
        time = distance / speed
        return time

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        mapping = {pos: speed[idx] for idx, pos in enumerate(position)}
        position.sort(reverse=True)

        fleet_stack: list[float] = []  # time to reach target

        for pos in position:
            time = self.get_time(mapping[pos], target - pos)
            fleet_stack.append(time)

            if len(fleet_stack) >= 2 and fleet_stack[-2] >= fleet_stack[-1]:
                fleet_stack.pop()

        return len(fleet_stack)
