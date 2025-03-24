# Priority Queue

A priority queue is an ADT that operates similar to a normal queue except that _each element has a certain priority_. The priorities of elements in a priority queue (PQ) determines the order in which elements are removed from the PQ.

NOTE: PQ only supports _"comparable data"_, meaning the data inserted into PQ should be able to order in some way either from least to greatest or vice-versa. This is so that we're able to assign relative priorities to each element.

**Questions**:

- How do the PQ knows which is the next smallest or the biggest element is to be removed?
- Does the machine resorts all the elements inside the PQ before polling operation?

Answer: Answer is No, because it is highly inefficient. Instead it uses something what is called as Heap.

## What is a heap?

A heap is a "tree" based data structure that satisfies the "heap invariant" (also called heap property) which is -- _"If A is a parent node of B then A is ordered with respect to B for all nodes A, B in the Heap."_

This property means that the value of Parent is greater than or equal to child node or the other way around.

This gives us two types of heap:

- Max Heap (Where parent node is always greater than the child node)
- Min Heap (Where parent node is always lesser than the child node)

Heap's forms the canonical underlying data structure for PQ and because of this PQ are sometime called as Heap's which is incorrect since PQ is an ADT (meaning that it can be implemented with other DS also).

NOTE:

- All heaps must be tree
- They should follow the heap invariant

## Where is a PQ used?

- Used in certain implementations of Dijkstra's Shortest Path Algorithm.
- Anytime you need the dynamically fetch the 'next best' or 'next worst' element.
- Used in Huffman coding (which is often used for lossless data compression).
  - Lossless compression is a class of data compression algorithms that allows the original data to be perfectly reconstructed from the compressed data.
- Best First Search (BFS) algorithms such as AStar use PQ to continuously grab the next most promising node.
- Used by Minimum Spanning Tree (MST) algorithms

## Time Complexities

| Operations                                   | Complexity |
| -------------------------------------------- | ---------- |
| Binary Heap construction                     | O(n)       |
| Polling                                      | O(log(n))  |
| Peeking                                      | O(1)       |
| Adding                                       | O(log(n))  |
| Naive removing                               | O(n)       |
| Advance removing with help from a hash table | O(log(n))  |
| Naive contains                               | O(n)       |
| Contains check with help of a hash table     | O(1)       |

Using a hash table to help optimize these operations does take up linear space and also adds some constant overhead to the binary heap implementation (because you're accessing your table a lot during swaps).

Also in time-complexity we have logarithmic time-complexity since we have to restore the heap invariant.

## Insertion

### Some terminologies to add elements to Binary Heap efficiently

NOTE: After reading this section if you want to know more about insertion in heap and view the `../heap/`.

1. Way of implementing a Priority Queue
    - PQs are usually implemented with heaps since this gives them the best possible time-complexity.
    - A PQ is an ADT, hence heaps are not the only way to implement PQs. As an example we can use unsorted list, but this would not give us the best possible time complexity.
    - NOTE: PQ != Heap

2. There are many types of heaps we could use to implement PQ
    - Binary Heap
    - Fibonacci Heap
    - Binomial Heap
    - Pairing Heap
    - So on...
    - For simplicity Binary Heap is good

3. Binary Heap:
    - A binary heap is a binary tree that supports the heap invariant. In a binary tree every node has exactly two children except for the last nodes where they can have at most 2 children.
    - The bottom heaps have children but they are None/Null
    - A "complete binary tree" is a tree in which at every level, except possibly the last, is completely filled and all the nodes are as far left as possible.
    - Whenever we insert node we insert them at the bottom row as far left to meet the complete binary tree property.
    - This property is important because it gives us the insertion point no matter what is the heap shape is or what values are in it.
    - We insert the element in the same row until the row is filled up and once it is filled we go to the next row.

        - Binary Heap Representation

            - Using an array is elegant and efficient way of doing this
            - We can also use the index, we go through heap one level from left to right at a time where index increases in same fashion.
            - Also storing Binary Heap in an array helps us to access all the children and parent node.

            ```text
            Let i be the parent node index:
            Left child index = 2i + 1
            Right child index = 2i + 2

            Zero based: Zero-based numbering or index origin = 0 is a way of numbering in which the initial element of a sequence is assigned the index 0).
            ```

4. NOTE:
    - Always maintain the heap invariant.
    - If you add element to binary heap and it breaks the heap invariant then it is of no use. So whenever you add elements to binary heap you need to swap each node upwards with its parent if it is smaller than its parent this is known bubbling up or swimming or shifting up.

## Deletion

When you want to remove the root node it is called as Polling.

Polling is done by following steps:

- Step 1: Remove root node.
- Step 2: Move the last element of last level to root.
- Step 3: Compare the value of this child node with its parent.
- Step 4: If value of parent is less than child, then swap them.
- Step 5: Repeat step 3 & 4 until Heap property holds.

When we want to remove any other node except the root node i.e. removing element from the Binary Heap:

- Step 1: We have to search for that value that we want to remove
- Step 2: Move the last element of last level to that position where the value that you want to remove is present.
- Step 3: Compare the value of this child node with its parent.
- Step 4: If value of parent is less than child, then swap them.
- Step 5: Repeat step 3 & 4 until Heap property holds.

Here, we have to bubble up or down or no need of bubbling as per conditions.

Here, time complexities will be something like this:

- Polling `O(log(n))`: Since we are directly swapping and then doing the bubbling.
- Removing `O(n)`: Since we have to do linear scan to find the element that we want to remove.

### Optimization by using HashTable

But there is a better of removing and improving the time complexity. The inefficiency of the removal algorithm comes from the fact that we have to perform linear search to find out where an element is present. Instead we did a lookup using a "Hashtable" to find out where a node is indexed at?

A hashtable provides a constant time lookup and update for a mapping from a key(the node value) to a value (the index).

Caveat: What if there are two or more nodes with the same value? - Dealing with the multiple value problem: Instead of mapping one value to one position we will map one value to multiple positions. We can maintain a "Set" or "Tree Set" of indexes for which a particular node value (key) maps to.

Example:

| Node Value | Position(s)/Index(es) |
| ---------- | --------------------- |
| (key)      | (value)               |
| 2          | 0, 2, 6               |
| 7          | 1, 4                  |
| 11         | 3                     |
| 13         | 5                     |

If we do swapping of 7 and 13 which are in positions 4 and 5 respectively then:

| Node | Position(s) |
| ---- | ----------- |
| 7    | 1, 5        |
| 13   | 4           |

Another question: If we want to remove a repeated node in our heap, which node do we remove and does it matter which one we pick? Answer: No it does not matter which node you remove as long as we satisfy the heap invariant in the end.

Example:

- Our PQ in binary heap form

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 0, 2, 6     |
| 7          | 1, 4        |
| 11         | 3           |
| 13         | 5           |

- Operation - insert(3)

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 0, 2, 6     |
| 7          | 1, 4        |
| 11         | 3           |
| 13         | 5           |
| 3          | 7           |

- Since heap invariant is not satisfied so we need to bubble up, After that we get:

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 0, 2, 6     |
| 7          | 3, 4        |
| 11         | 7           |
| 13         | 5           |
| 3          | 1           |

- Operation - remove(2)
- Which should be removed doesn't matter as long as we satisfy the heap invariant, So if we remove the 2 at position 0 we will get

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 2, 6        |
| 7          | 3, 4        |
| 11         | 0           |
| 13         | 5           |
| 3          | 1           |

- Now we have to satisfy the heap invariant, After satisfying we get

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 0, 2        |
| 7          | 3, 4        |
| 11         | 6           |
| 13         | 5           |
| 3          | 1           |

- Operation - poll()

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 6, 2        |
| 7          | 3, 4        |
| 11         | 0           |
| 13         | 5           |
| 3          | 1           |

- Now polling 2

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 2           |
| 7          | 3, 4        |
| 11         | 0           |
| 13         | 5           |
| 3          | 1           |

- Now we have to satisfy the heap invariant, After satisfying we get

| Node Value | Position(s) |
| ---------- | ----------- |
| 2          | 0           |
| 7          | 3, 4        |
| 11         | 2           |
| 13         | 5           |
| 3          | 1           |

## Convert min PQ to max PQ

Why you need to know how to convert min PQ to max PQ? In standard library of most programming languages we only get min PQ, but sometimes we need a max PQ.

Since elements in a priority queue are comparable they implement some sort of "comparable interface" which we can simply "negate" to achieve a Max heap.

### First Way

Let x, y be numbers in the PQ. For a min PQ, if x<=y then x comes out of the PQ before y, so the negation of this is if x>=y then y comes out before x.

NOTE: negation of x<=y is x>y but we have used x>=y, well that one is not for comparators, if x=y wether or not comparator is negated x will still be equal to y.

### Alternative method

In this method we negate the numbers as we insert them into the PQ and negate them again when they are taken out. This has the same effect as negating the comparators.

#### Understanding the way of converting heap from min to max

Suppose "lex" is a comparator for strings which sorts strings in lexicographic order (the default in most programming languages). Then let "nlex" be the negation of "lex", also let s1 and s2 be strings.

```text
lex(s1, s2) = -1 if s1<s2 lexicographically
lex(s1, s2) = 0  if s1=s2 lexicographically
lex(s1, s2) = +1 if s1>s2 lexicographically
```

```text
nlex(s1, s2) = -(-1) = +1 if s1<s2 lexicographically
nlex(s1, s2) = -(0)  = 0  if s1=s2 lexicographically
nlex(s1, s2) = -(+1) = -1 if s1>s2 lexicographically
```

```text
Example:
    Strings - XX, A, XR, X, B, FZ

    While using lex comparator:
        Order - A, B, FZ, X, XR, XX
    While using nlex comparator:
        Order - XX, XR, X, FZ, B, A
```
