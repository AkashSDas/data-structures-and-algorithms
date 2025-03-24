import pytest
from src.data_structures.graph.bidirectional_graph import BidirectionalGraph


@pytest.fixture
def graph():
    g = BidirectionalGraph()
    return g


def test_add_vertex(graph):
    graph.add_vertex("A")
    assert "A" in graph.adjacency_list
    assert graph.adjacency_list["A"] == []


def test_add_edge(graph):
    graph.add_edge("A", "B", 1)
    assert {"vertex": "B", "weight": 1} in graph.adjacency_list["A"]
    assert {"vertex": "A", "weight": 1} in graph.adjacency_list["B"]


def test_remove_edge(graph):
    graph.add_edge("A", "B", 1)
    graph.remove_edge("A", "B")
    assert not any(edge["vertex"] == "B" for edge in graph.adjacency_list["A"])
    assert not any(edge["vertex"] == "A" for edge in graph.adjacency_list["B"])


def test_remove_vertex(graph):
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 2)
    graph.remove_vertex("A")
    assert "A" not in graph.adjacency_list
    assert not any(edge["vertex"] == "A" for edge in graph.adjacency_list["B"])
    assert not any(edge["vertex"] == "A" for edge in graph.adjacency_list["C"])


def test_depth_first_search(graph):
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "E", 1)
    result = graph.depth_first_search("A")
    assert result == ["A", "C", "E", "B", "D"]


def test_breadth_first_search(graph):
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "E", 1)
    result = graph.breadth_first_search("A")
    assert result == ["A", "B", "C", "D", "E"]


def test_dijkstra(graph):
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)
    result = graph.dijkstra("A", "D")
    assert result == ["A", "B", "C", "D"]


def test_nonexistent_vertex_operations(graph):
    graph.add_vertex("A")
    graph.remove_edge("A", "B")  # Should handle gracefully
    graph.remove_vertex("B")  # Should handle gracefully
    assert "A" in graph.adjacency_list
    assert "B" not in graph.adjacency_list
