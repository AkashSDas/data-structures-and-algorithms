type StackNode<T> = {
    value: T;
    next: StackNode<T> | undefined;
};

interface IStack<T> {
    size: number;

    push(value: T): void;
    pop(): StackNode<T> | undefined;
    peek(): StackNode<T> | undefined;
    find(value: T): StackNode<T> | undefined;

    [Symbol.iterator](): IterableIterator<T>;
    toList(): T[];
}

/**
 * Stack implementation using a linked list.
 * Head is the top of the stack. Insertion and deletion happens at the head.
 * @example (head) 3 -> 2 -> 1
 */
export class Stack<T> implements IStack<T> {
    size: number;
    private head: StackNode<T> | undefined;

    constructor() {
        this.size = 0;
        this.head = undefined;
    }

    push(value: T): void {
        const node: StackNode<T> = { value, next: this.head };
        this.head = node;
        this.size++;
    }

    pop(): StackNode<T> | undefined {
        if (!this.head) return undefined;
        const node = this.head;
        this.head = node.next;
        this.size--;
        return node;
    }

    peek(): StackNode<T> | undefined {
        return this.head;
    }

    find(value: T): StackNode<T> | undefined {
        let currNode = this.head;

        while (currNode) {
            if (currNode.value === value) {
                return currNode;
            } else {
                currNode = currNode.next;
            }
        }

        return undefined;
    }

    *[Symbol.iterator](): IterableIterator<T> {
        let currNode = this.head;

        while (currNode) {
            yield currNode.value;
            currNode = currNode.next;
        }

        return undefined;
    }

    toList(): T[] {
        const list: T[] = [];
        let currNode = this.head;

        while (currNode) {
            list.push(currNode.value);
            currNode = currNode.next;
        }

        return list;
    }
}
