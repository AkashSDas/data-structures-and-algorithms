# Binary Search Tree

## Insertion

In BST, elements must be **comparable** so that we can order them. When an element is inserted in the BST, its value is compared to the value stored in the current node. For this we have to consider the following cases:

- Case `new < current` - Recurse on the left subtree
- Case `new > current` - Recurse on the right subtree
- Case `new == current` - Do nothing (handle duplicate values)

## Deletion

The process of removing an element from BST has 2 processes:

- Finding the element (if it exists)
- Replace the node to be deleted with its successor (if any) to maintain the BST invariant

### Finding the element

When finding the node to be deleted, any of the following 4 things can happen:

- We hit the `null` node at the end of the tree, which means the node to be deleted doesn't exist
- Comparators value `equal to 0` (found it)
- Comparator value `less than 0` (the value, if it exists, is in the left subtree)
- Comparator value `greater than 0` (the value, if it exists, is in the right subtree)

### Removing the element

There are 4 cases while removing a node:

- Node to be removed is a leaf node
- Node to be removed has a right subtree but no left subtree
- Node to be removed has a left subtree but no right subtree
- Node to be removed has both the left and right subtrees

**Case 1 - Leaf node** - If the node we wish to remove is a leaf node then we may do so without any problem.

**Case 2 and 3 - only one successor** - Either the left/right child node is a subtree. The successor of the node we are trying to remove in these cases will be the root node of the left/right subtree. It may be the case that we are removing the root node of the BST in this case its immediate child becomes the new root as we would except.

**Case 4 - node to remove has a both left and right subtrees** - Which subtree will be the successor of the node we are trying to remove be? The answer is both, the successor can either be the **largest value in the left subtree** OR the **smallest value in the right subtree**.

A justification for why there could be more than one successor is:

- The largest value in the left subtree satisfies the BST invariant since it. Its larger than everything in left subtree. This follows immediately from the definition of being the largest. Its smaller than everything found in right subtree because it was found in the left subtree.
- Similarly, the smallest value in the right subtree satisfies the BST invariant since its smaller than everything in right subtree. This follows immediately from the definition of being the smallest. Its larger than everything found in left subtree because it was found in the right subtree.

Conclusion - Therefore there are two possible successors.

## Difference between Binary Tree and Binary Search Tree

A Binary Tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

A Binary Search Tree (BST) is a type of binary tree with special properties. In a BST, all nodes to the left of a node have values less than the node's value, and all nodes to the right have values greater than the node's value. This property must be true for all nodes in the tree.

So, while every BST is a binary tree, not every binary tree is a BST. The main difference lies in the property that BST upholds to maintain a sorted order of elements, which is not a requirement in a general binary tree.

## Time Complexity

The time complexity of searching in a Binary Search Tree (BST) is O(h), where h is the height of the tree.

In the best-case scenario, when the tree is a balanced binary search tree, the height of the tree is log(n), where n is the number of nodes. So, the best-case time complexity is O(log(n)).

In the worst-case scenario, when the tree is a skewed binary tree (all the nodes are in one straight line like a linked list), the height of the tree is n. So, the worst-case time complexity is O(n).

Therefore, the time complexity of searching in a BST can range from O(log(n)) to O(n), depending on how balanced the tree is.
