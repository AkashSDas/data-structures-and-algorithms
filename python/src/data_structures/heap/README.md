# Heap

NOTE: Don't compare heap with any other trees. Heap is a special kind of tree which is used to implement priority queue. Its not an ADT.

Heap is a complete binary tree which means that each node will have two children at max. While creating a complete binary tree fill the left child (for that node) and then right child (for that node) and then move to other nodes.

```text
      o             o               o                  o              o             o
           =>     /        =>     /    \      =>     /   \     =>   /   \    =>   /   \
                 o               o      o           o     o        o     o       o     o
                                                   /              / \           / \
                                                  o              o   o         o   o
                                                                              /
                                                                             o
```

## Max and Min

### Max

Here root node value is greater than both child node's values.

```text
          30
      /       \
     20       15
    /  \     /  \
   5   10   13   6
```

### Min

Here root node value is smaller than both child node's values.

```text
          5
      /       \
     15       13
    /  \     /  \
  20   25   30   17
```

## Insertion

While adding values to heap follow the complete binary tree property i.e. fill left child (of a node) then fill right child (of that node) and then move other node in the same level and if you've filled all the nodes in current level then move to the next level.

In the below example we're working with Max Heap Tree.

```text
               30
            /      \
          20        15
         /  \      /  \
        5   10    12   6
```

Insert 25

```text
               30
            /      \
          20        15
         /  \      /  \
        5   10    12   6
       /
      25
```

Since insertion of 25 violates the max heap property, we've to do some changes. So compare 25 with its root and see if it is smaller than 25 if yes then exchange values and do this till you either become the top root or the root is bigger than 25. (In min heap it would check if the value is bigger, if yes then move up it either the root value is smaller than inserted value or when inserted value becomes the top root)

```text
               30
            /      \
          20        15
         /  \      /  \
       25   10    12   6
       /
      5
```

```text
               30
            /      \
           25       15
         /  \      /  \
       20   10    12   6
       /
      5
```

## Deletion

In the below example we're working with Max Heap Tree.

```text
               30
            /      \
          20        15
         /  \      /  \
        5   10    12   6
```

The main issue with deletion is that we cannot delete any value we want. We've to delete a very specific node in our and that is the root node.

Once you delete the root node, add new root node from the node which balances the tree (min or max) and search for that node from the bottom the level to the top level.

Delete root node i.e. 30

```text
               6
            /      \
          20        15
         /  \      /
        5   10    12
```

Now since the deletion of 30 and addition of 6 as new root disturbs the max heap property so compare it with its children (starting from left and then right) and see which one is bigger, if none of them are bigger the max heap property is consistent but if any child is bigger then exchange values between root and that child and now treat that child as root and do the same process with its child. For min heap it will checking if any child value is smaller.

```text
               20
            /      \
           6        15
         /  \      /
        5   10    12
```

```text
               20
            /      \
          10        15
         /  \      /
        5    6    12
```
