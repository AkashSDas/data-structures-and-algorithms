import pytest

from src.data_structures.binary_search_tree.binary_search_tree import Tree


@pytest.fixture
def sample_tree():
    tree = Tree()
    root = tree.insert(10, None)
    tree.insert(5, root)
    tree.insert(15, root)
    tree.insert(3, root.left)
    tree.insert(7, root.left)
    tree.insert(12, root.right)
    tree.insert(18, root.right)
    return tree


def test_insert_root():
    tree = Tree()
    root = tree.insert(10, None)
    assert root.val == 10
    assert tree.root == root


def test_insert_left_and_right():
    tree = Tree()
    root = tree.insert(10, None)
    left = tree.insert(5, root)
    right = tree.insert(15, root)
    assert root.left == left
    assert root.right == right
    assert left.val == 5
    assert right.val == 15


def test_insert_duplicate_raises_exception():
    tree = Tree()
    root = tree.insert(10, None)
    with pytest.raises(Exception, match="Duplicate values are not allowed"):
        tree.insert(10, root)


def test_find_existing_node(sample_tree):
    node, parent = sample_tree.find(7, sample_tree.root)
    assert node is not None
    assert node.val == 7
    assert parent.val == 5


def test_find_non_existing_node(sample_tree):
    node, parent = sample_tree.find(100, sample_tree.root)
    assert node is None
    assert parent is None


def test_delete_leaf_node(sample_tree):
    sample_tree.delete(3)  # Leaf node
    assert sample_tree.traverse_in_order() == [5, 7, 10, 12, 15, 18]


def test_delete_node_with_one_child():
    tree = Tree()
    root = tree.insert(10, None)
    tree.insert(5, root)
    tree.insert(3, root.left)  # 5 has one child (3)
    tree.delete(5)
    assert tree.traverse_in_order() == [3, 10]


def test_delete_node_with_two_children(sample_tree):
    sample_tree.delete(5)  # 5 has two children (3 and 7)
    assert sample_tree.traverse_in_order() == [3, 7, 10, 12, 15, 18]


def test_delete_root_node_with_two_children(sample_tree):
    sample_tree.delete(10)  # Root has two children
    assert sample_tree.traverse_in_order() == [3, 5, 7, 12, 15, 18]


def test_delete_non_existing_value(sample_tree):
    with pytest.raises(AssertionError, match="Value doesn't exists in the tree"):
        sample_tree.delete(100)


def test_traverse_in_order(sample_tree):
    assert sample_tree.traverse_in_order() == [3, 5, 7, 10, 12, 15, 18]


def test_traverse_pre_order(sample_tree):
    assert sample_tree.traverse_pre_order() == [10, 5, 3, 7, 15, 12, 18]


def test_traverse_post_order(sample_tree):
    assert sample_tree.traverse_post_order() == [3, 7, 5, 12, 18, 15, 10]


def test_invert_tree(sample_tree):
    sample_tree.invert_tree()
    # After invert:
    # Original: 10 -> left 5, right 15
    # Inverted: 10 -> left 15, right 5
    assert sample_tree.root.left.val == 15
    assert sample_tree.root.right.val == 5
    # Check one deeper level
    assert sample_tree.root.left.left.val == 18
    assert sample_tree.root.left.right.val == 12
    assert sample_tree.root.right.left.val == 7
    assert sample_tree.root.right.right.val == 3
