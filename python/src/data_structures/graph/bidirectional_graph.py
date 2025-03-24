import heapq
from typing import TypedDict


class AdjacencyVertex(TypedDict):
    vertex: str
    weight: float


class BidirectionalGraph:
    def __init__(self) -> None:
        self.adjacency_list: dict[str, list[AdjacencyVertex]] = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex: str, to_vertex: str, weight: float) -> None:
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

        self.adjacency_list[from_vertex].append({"vertex": to_vertex, "weight": weight})
        self.adjacency_list[to_vertex].append({"vertex": from_vertex, "weight": weight})

    def remove_edge(self, from_vertex: str, to_vertex: str) -> None:
        if from_vertex in self.adjacency_list:
            self.adjacency_list[from_vertex] = list(
                filter(
                    lambda e: e["vertex"] != to_vertex,
                    self.adjacency_list[from_vertex],
                )
            )

        if to_vertex in self.adjacency_list:
            self.adjacency_list[to_vertex] = list(
                filter(
                    lambda e: e["vertex"] != from_vertex,
                    self.adjacency_list[to_vertex],
                )
            )

    def remove_vertex(self, vertex: str) -> None:
        if vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                self.remove_edge(vertex, adjacent["vertex"])

            del self.adjacency_list[vertex]

    def depth_first_search(self, start_vertex: str) -> list[str]:
        visited: list[str] = []
        stack: list[str] = [start_vertex]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.append(vertex)

                for neighbor in self.adjacency_list[vertex]:
                    stack.append(neighbor["vertex"])

        return visited

    def breadth_first_search(self, start_vertex: str) -> list[str]:
        visited: list[str] = []
        queue: list[str] = [start_vertex]

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited:
                visited.append(vertex)

                for neighbor in self.adjacency_list[vertex]:
                    queue.append(neighbor["vertex"])

        return visited

    def dijkstra(self, start_vertex: str, end_vertex: str) -> list[str]:
        # Distance from startVertex to vertex, {vertex, distance to reach there}
        distances: dict[str, float] = {
            vertex: float("inf") for vertex in self.adjacency_list
        }

        # Previous vertex in the shortest path {to: from}
        previous: dict[str, str | None] = {
            vertex: None for vertex in self.adjacency_list
        }

        distances[start_vertex] = 0
        heap = [(distances[start_vertex], start_vertex)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.adjacency_list[current_vertex]:
                distance = current_distance + neighbor["weight"]

                if distance < distances[neighbor["vertex"]]:
                    distances[neighbor["vertex"]] = distance
                    previous[neighbor["vertex"]] = current_vertex
                    heapq.heappush(heap, (distance, neighbor["vertex"]))

        # Get the shortest path

        shortest_path: list[str] = []
        curr = end_vertex

        while previous[curr] is not None:
            shortest_path.append(curr)

            next_vertex = previous[curr]
            if next_vertex:
                curr = next_vertex

        if curr == start_vertex:
            shortest_path.append(curr)

        shortest_path.reverse()
        return shortest_path
