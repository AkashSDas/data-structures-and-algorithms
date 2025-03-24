# Graph

## Introduction

A graph is a **non-linear data structure** consisting of a set of vertices (or nodes) and a set of edges that connect these vertices. It is used to represent relationships between different entities.

## Terminologies

- **Vertex**: Also known as a node, it represents an entity in the graph.
- **Edge**: It represents a connection between two vertices.
- **Directed Graph**: A graph in which edges have a specific direction.
- **Undirected Graph**: A graph in which edges have no direction.
- **Weighted Graph**: A graph is which edges have weights or costs associated with them.
- **Adjacency Matrix**: A matrix representation of a graph where each cell represents whether there is an edge between two vertices.
- **Adjacency List**: A list representation of a graph where each vertex has a list of its adjacent vertices.

Example of Adjacency Matrix:

A matrix representing the graph (Directed Weighted Example):

| A   | B   | C   | D   |     |
| --- | --- | --- | --- | --- |
| A   | 0   | 5   | 0   | 0   |
| B   | 0   | 0   | 3   | 1   |
| C   | 0   | 0   | 0   | 2   |
| D   | 4   | 0   | 0   | 0   |

- Each row is the source vertex.
- Each column is the destination vertex.
- The value is the weight (0 means no edge).

Example of Adjacency List where we've a list of neighbors for each vertex:

```text
A: [(B, 5)]
B: [(C, 3), (D, 1)]
C: [(D, 2)]
D: [(A, 4)]
```

- Each vertex points to its connected vertices along with edge weights.

## Concepts

- **Connectivity**: Determines whether there is a path between two vertices.
- **Cycle**: A path starts and ends at the same vertex.
- **Degree**: The number of edges connected to a vertex.
- **Path**: A sequence of vertices connected by edges.
- **Shortest Path**: The path with the minimum number of edges or minimum total weight.

## Time Complexities

| Operations  | Directed Graph | Undirected Graph |
| ----------- | -------------- | ---------------- |
| Search      | O(V + E)       | O(V + E)         |
| Insert Node | O(1)           | O(1)             |
| Insert Edge | O(1)           | O(1)             |
| Remove Node | O(V + E)       | O(V + E)         |
| Remove Edge | O(E)           | O(E)             |

`V` is the number of vertices and `E` is the number of edges. The complexity of search operation is `O(V + E)` because in the worst case we may need to visit all vertices and edges of the graph. The complexity of remove edge is `O(E)` because we need to find the edge in the list of edges. The complexity of remove node is `O(V + E)` because we need to remove the node and all its associated edges.

## Use Cases

Graphs are used in various real-world scenarios, including:

- Social networks
- Routing algorithms
- Web page ranking algorithms
- Recommendation systems
- Network analysis

## Dijkstra's algorithm pseudo-code

```text
function dijkstra(graph, source):
    dist[source] = 0
    for each vertex v in graph:
        if v != source:
            dist[v] = INFINITY
        add v to priority queue
    while priority queue is not empty:
        u = vertex in priority queue with minimum distance
        remove u from priority queue
        for each neighbor v of u:
            alt = dist[u] + weight(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                decrease priority of v in queue
    return dist, prev
```
