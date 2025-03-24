from collections import defaultdict
import math
import heapq


class Solution:
    def get_plane_distance(self, x: int, y: int) -> float:
        return math.sqrt((x**2) + (y**2))

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        plane_dists: dict[float, list[tuple[int, int]]] = defaultdict(list)

        for x, y in points:
            dist = self.get_plane_distance(x, y)
            plane_dists[dist].append((x, y))

        min_heap = list(plane_dists.keys())
        heapq.heapify(min_heap)

        result: list[list[int]] = []

        idx = 0
        while min_heap and idx != k:
            plane = heapq.heappop(min_heap)
            matching_points = [list(pts) for pts in plane_dists[plane]]
            left_entires = k - len(result)

            if left_entires <= 0:
                break
            elif len(matching_points) <= left_entires:
                result.extend(matching_points)
                idx += len(matching_points)
            elif len(matching_points) > left_entires:
                result.extend(matching_points[:left_entires])
                idx += left_entires

        return result
