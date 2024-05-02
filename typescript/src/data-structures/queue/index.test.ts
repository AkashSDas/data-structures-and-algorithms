import { Queue } from ".";

describe("Queue", () => {
    it("should create empty queue", () => {
        var queue = new Queue<number>();
        expect(queue.size).toBe(0);
        expect(queue.peek()).toBeUndefined();
    });

    it("should enqueue items to queue", () => {
        var queue = new Queue<number>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        expect(queue.size).toBe(3);
        expect(queue.peek()?.value).toBe(1);
    });

    it("should dequeue items from queue", () => {
        var queue = new Queue<number>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        expect(queue.dequeue()?.value).toBe(1);
        expect(queue.dequeue()?.value).toBe(2);
        expect(queue.dequeue()?.value).toBe(3);
        expect(queue.dequeue()).toBeUndefined();
        expect(queue.size).toBe(0);
    });

    it("should find items in queue", () => {
        var queue = new Queue<number>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        expect(queue.find(2)?.value).toBe(2);
        expect(queue.find(4)).toBeUndefined();
    });

    it("should iterate over queue", () => {
        var queue = new Queue<number>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        var items = [];
        for (let item of queue) {
            items.push(item);
        }
        expect(items).toEqual([1, 2, 3]);
    });

    it("should convert queue to list", () => {
        var queue = new Queue<number>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        expect(queue.toList()).toEqual([1, 2, 3]);
    });
});
