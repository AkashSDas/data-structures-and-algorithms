from typing import TypedDict


class AdjacencyVertex(TypedDict):
    vertex: str
    weight: int


class Graph:
    def __init__(self) -> None:
        self.adjacency_list: dict[str, list[AdjacencyVertex]] = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex: str, to_vertex: str, weight: int) -> None:
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)

        self.adjacency_list[from_vertex].append({"vertex": to_vertex, "weight": weight})

    def remove_edge(self, from_vertex: str, to_vertex: str) -> None:
        if from_vertex in self.adjacency_list:
            self.adjacency_list[from_vertex] = list(
                filter(
                    lambda e: e["vertex"] != to_vertex,
                    self.adjacency_list[from_vertex],
                )
            )

    def remove_vertex(self, vertex: str) -> None:
        if vertex in self.adjacency_list:
            for from_vertex in self.adjacency_list:
                self.remove_edge(from_vertex, vertex)

            del self.adjacency_list[vertex]

    def depth_first_search(self, start_vertex: str) -> list[str]:
        visited: list[str] = []
        queue: list[str] = []
        queue.append(start_vertex)

        while len(queue) > 0:
            vertex = queue.pop()

            if vertex not in visited:
                visited.append(vertex)

                for edges in self.adjacency_list[vertex]:
                    queue.append(edges["vertex"])

        return visited

    def breadth_first_search(self, start_vertex: str) -> list[str]:
        visited: list[str] = []
        stack: list[str] = []
        stack.append(start_vertex)

        while len(stack) > 0:
            vertex = stack.pop(0)

            if vertex not in visited:
                visited.append(vertex)

                for edges in self.adjacency_list[vertex]:
                    stack.append(edges["vertex"])

        return visited

    # https://www.youtube.com/watch?v=EFg3u_E6eHU
    def dijkstra(self, start_vertex: str, end_vertex: str) -> list[str]:
        # Distance from startVertex to vertex, {vertex, distance to reach there}
        distances: dict[str, float] = {}

        # Previous vertex in the shortest path {to: from}
        previous: dict[str, str | None] = {}

        visited: list[str] = []
        queue: list[str] = []

        # Initialize distances and previous
        for vertex in self.adjacency_list:
            distances[vertex] = float("inf")
            previous[vertex] = None

        distances[start_vertex] = 0
        queue.append(start_vertex)

        while len(queue) > 0:
            vertex = queue.pop(0)
            edges = self.adjacency_list[vertex]

            for edge in edges:
                distance = distances[vertex] + edge["weight"]

                # If the distance is less than the current distance, update the distance and previous
                if distance < distances[edge["vertex"]]:
                    distances[edge["vertex"]] = distance
                    previous[edge["vertex"]] = vertex

                if edge["vertex"] not in visited:
                    queue.append(edge["vertex"])

            visited.append(vertex)

        # Get the shortest path

        shortest_path: list[str] = []
        curr_vertex = end_vertex

        while curr_vertex != start_vertex:
            shortest_path.append(curr_vertex)
            next_vertex = previous[curr_vertex]

            if next_vertex:
                curr_vertex = next_vertex

        shortest_path.reverse()
        return shortest_path
