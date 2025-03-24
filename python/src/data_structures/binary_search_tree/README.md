# Tree

## Terminology

A "tree" is an "undirected graph" which satisfies any of the following definitions.

- An acyclic connected graph.
- A connected graph with N nodes and N-1 edges.
- An graph in which any two vertices are connected by exactly one path.

### Root Node

- The root serves as a point of reference for other vertices in the tree.
- If we have a "rooted tree" then we will want to have a reference to the root node of our tree.
- It does not always matter which node is selected to be the root node because any node can root the tree (any node can become the root of the tree).

### Child and Parent Node

- A "child" is a node extending from another node.
- A "parent" is the inverse of this.

What is the parent of the root node? It has no parent, although it may be useful to assign the parent of the node to be itself (e.g. filesystem tree).

### Leaf node

A "leaf node" is a node with no child.

### Subtree

A "subtree" is a tree entirely contained within another.

NOTE - Subtrees may consist of a single node.

## Binary Tree

What is a binary tree? A "binary tree" is a tree for which every node has at most two child nodes.

What is a binary search tree (BST)? A "binary search tree" is a binary tree that satisfies the "BST invariant" which is "left subtree has smaller elements and right subtree has larger elements".

BST operations allow for duplicate values, but most of the time we are only interested in having unique elements inside our tree.

## What are Binary Trees used for?

- Implementation of some map and set ADTs
- Red Black Trees
- AVL Trees
- Splay Trees

- Used in the implementation of binary heaps
- Syntax trees (used by compiler and calculators)
- Treap - a probabilistic Data Structure (used a randomized BST)

## Time Complexity of Binary Search Tree

| Operation | Average   | Worst |
| --------- | --------- | ----- |
| Insert    | O(log(n)) | O(n)  |
| Delete    | O(log(n)) | O(n)  |
| Remove    | O(log(n)) | O(n)  |
| Search    | O(log(n)) | O(n)  |

O(log(n)) is good but O(n) is really bad
