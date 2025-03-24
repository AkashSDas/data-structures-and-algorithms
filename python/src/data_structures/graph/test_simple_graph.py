import pytest

from src.data_structures.graph.simple_graph import Graph


@pytest.fixture
def sample_graph():
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)
    g.add_edge("D", "F", 11)
    return g


def test_add_vertex():
    g = Graph()
    g.add_vertex("X")
    assert "X" in g.adjacency_list
    assert g.adjacency_list["X"] == []


def test_add_edge():
    g = Graph()
    g.add_edge("X", "Y", 5)
    assert g.adjacency_list["X"] == [{"vertex": "Y", "weight": 5}]
    assert "Y" in g.adjacency_list  # Y should exist


def test_remove_edge():
    g = Graph()
    g.add_edge("X", "Y", 5)
    g.remove_edge("X", "Y")
    assert g.adjacency_list["X"] == []


def test_remove_vertex():
    g = Graph()
    g.add_edge("X", "Y", 5)
    g.add_edge("Y", "X", 2)
    g.remove_vertex("X")
    assert "X" not in g.adjacency_list
    assert g.adjacency_list["Y"] == []


def test_depth_first_search(sample_graph):
    dfs_result = sample_graph.depth_first_search("A")
    assert dfs_result[0] == "A"
    assert "D" in dfs_result
    assert "F" in dfs_result
    assert sorted(dfs_result) == ["A", "B", "C", "D", "E", "F"]  # all vertices visited


def test_breadth_first_search(sample_graph):
    bfs_result = sample_graph.breadth_first_search("A")
    assert bfs_result[0] == "A"
    assert "D" in bfs_result
    assert "F" in bfs_result
    assert sorted(bfs_result) == ["A", "B", "C", "D", "E", "F"]


def test_dijkstra(sample_graph):
    shortest_path = sample_graph.dijkstra("A", "D")
    assert shortest_path == ["C", "E", "D"]  # A->C->E->D
