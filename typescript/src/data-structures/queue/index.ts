type QueueNode<T> = {
    value: T;
    next: QueueNode<T> | undefined;
};

interface IQueue<T> {
    size: number;

    enqueue(value: T): void;
    dequeue(): QueueNode<T> | undefined;
    peek(): QueueNode<T> | undefined;
    find(value: T): QueueNode<T> | undefined;

    [Symbol.iterator](): IterableIterator<T>;
    toList(): T[];
}

/**
 * Queue implementation using a linked list.
 * Head is the top of the queue. Deletion happens at the head and insertion happens at the tail.
 * @example (head) 3 -> 2 -> 1 (tail)
 */
export class Queue<T> implements IQueue<T> {
    size: number;
    private head: QueueNode<T> | undefined;

    constructor() {
        this.size = 0;
        this.head = undefined;
    }

    enqueue(value: T): void {
        const node: QueueNode<T> = { value, next: undefined };

        if (!this.head) {
            this.head = node;
        } else {
            let currNode = this.head;

            while (currNode.next) {
                currNode = currNode.next;
            }

            currNode.next = node;
        }

        this.size++;
    }

    dequeue(): QueueNode<T> | undefined {
        if (!this.head) return undefined;
        const node = this.head;
        this.head = this.head.next;
        this.size--;
        return node;
    }

    peek(): QueueNode<T> | undefined {
        return this.head;
    }

    find(value: T): QueueNode<T> | undefined {
        let node = this.head;
        while (node) {
            if (node.value === value) return node;
            node = node.next;
        }
        return undefined;
    }

    *[Symbol.iterator](): IterableIterator<T> {
        let node = this.head;

        while (node) {
            yield node.value;
            node = node.next;
        }

        return undefined;
    }

    toList(): T[] {
        const list: T[] = [];
        let node = this.head;

        while (node) {
            list.push(node.value);
            node = node.next;
        }

        return list;
    }
}
