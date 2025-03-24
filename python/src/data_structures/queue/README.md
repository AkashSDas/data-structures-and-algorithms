# Queue

A queue is a linear data structure which models real world queues by having two primary operations namely **enqueue** and **dequeue**.

Insertion and deletion happens in different ends. The insertion happens at the **rear** end and deletion happens at the **front** end.

## Terminologies

- **Front**: The front end of the queue where the elements are removed.
- **Rear**: The rear end of the queue where the elements are inserted.
- **Enqueue**: Inserting an element at the rear end of the queue.
- **Dequeue**: Removing an element from the front end of the queue.

There no consistency in terminologies for inserting and removing elements from queues. Enqueue = Adding = Offering and Dequeue = Removing = Polling (but this can cause ambiguity that do they want to remove from back OR from the entire queue).

## Where are queues used?

- Any waiting line models a queue
- Can be used to effectively keep track of the x(anything) most recently added elements.
- Web server request management where you want first come first serve
- Breadth First Search (BFS) graph traversal

## Time Complexity

| Operations | Complexity |
| ---------- | ---------- |
| Enqueue    | O(1)       |
| Dequeue    | O(1)       |
| Peeking    | O(1)       |
| Contains   | O(n)       |
| Removal    | O(n)       |
| Is Empty   | O(1)       |

## Example

Implementation in Breadth First Search.

```text
Algorithm:
    Let Q be a Queue
    Q.enqueue(starting_node)
    starting_node = true

    While Q is not empty Do
        node = Q.dequeue()
        For neighbor in neighbors(node):
            If neighbor has not been visited:
                neighbor.visited = true
                Q.enqueue(neighbor2)
```
