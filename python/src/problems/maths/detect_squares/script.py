from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.point_counts: dict[tuple, int] = defaultdict(int)
        self.points: list[list[int]] = []

    def add(self, point: list[int]) -> None:
        self.point_counts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: list[int]) -> int:
        result = 0
        qx, qy = point

        for px, py in self.points:
            if (abs(py - qy) != abs(px - qx)) or px == qx or py == qy:
                continue

            result += self.point_counts[(qx, py)] * self.point_counts[(px, qy)]

        return result
