# Tree Traversal

## Ways of tree traversal

- Depth First Search:
    1. Preorder
    2. Inorder
    3. Postorder
- Breadth First Search:
    1. Level Order

## Depth First Search

Preorder, Inorder, Postorder -- These three types of traversals are naturally defined recursively:

```text
Preorder prints before the recursive calls preorder(node):
    if node == null: return
    print(node.value)
    preorder(node.left)
    preorder(node.right)
```

```text
Inorder prints between the recursive calls inorder(node):
    if node == null: return
    inorder(node.left)
    print(node.value)
    inorder(node.right)
```

```text
Postorder prints after the recursive calls postorder(node):
    if node == null: return
    postorder(node.left)
    postorder(node.right)
    print(node.value)
```

```text
        Example:
                    1
                  /   \
                2       3
              /   \
            4       5

            - Inorder   (Left, Root, Right) : 4 2 5 1 3
            - Preorder  (Root, Left, Right) : 1 2 4 5 3
            - Postorder (Left, Right, Root) : 4 5 2 3 1
```

## Breadth First Search

Level Order Traversal - In level order traversal we want to print the nodes as they appear one layer at a time.

```text
    Example:

                    1
                  /   \
                2       3
              /   \
            4       5
```

Level Order Traversal : 1 2 3 4 5

- To obtain this ordering we want to do a Breadth First Search(BFS) from the root node down to the leaf modes.
- To do a BFS we will need to maintain a "Queue" of the nodes left to explore.
- Begin with the root inside of the queue and finish when the queue is empty.

```text
    Example:
                        11
                      /    \
                    6       15
                  /  \     /   \
                 3    8   13   17
               /   \     /  \    \
              1     5   12  14   19

            At each iteration we add the left child and the the right
            child of the current node to our Queue

            1. Queue - 11
               Order -

            2. Adding 11's children to the queue
               Queue - 6, 15
               Order - 11

            3. Adding 6's children to the queue
               Queue - 15, 3, 8
               Order - 11, 6

            4. Adding 15's children to the queue
               Queue - 3, 8, 13, 17
               Order - 11, 6, 15

            5. Adding 3's children to the queue
               Queue - 8, 13, 17, 1, 5
               Order - 11, 6, 15, 3

            6. Here 8 has no child
               Queue - 13, 17, 1, 5
               Order - 11, 6, 15, 3, 8

            7. Adding 13's children to the queue
               Queue - 17, 1, 5, 12, 14
               Order - 11, 6, 15, 3, 8, 13

            8. Adding 17's children to the queue
               Queue - 1, 5, 12, 14, 19
               Order - 11, 6, 15, 3, 8, 13, 17

            9. Now emptying the queue
               Queue -
               Order - 11, 6, 15, 3, 8, 13, 17, 1, 5, 12, 14, 19
```
