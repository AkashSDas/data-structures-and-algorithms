import { Stack } from ".";

describe("Stack", () => {
    it("should create empty stack", () => {
        var stack = new Stack<number>();
        expect(stack.size).toBe(0);
        expect(stack.peek()).toBeUndefined();
    });

    it("should push items to stack", () => {
        var stack = new Stack<number>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        expect(stack.size).toBe(3);
        expect(stack.peek()?.value).toBe(3);
    });

    it("should pop items from stack", () => {
        var stack = new Stack<number>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        expect(stack.pop()?.value).toBe(3);
        expect(stack.pop()?.value).toBe(2);
        expect(stack.pop()?.value).toBe(1);
        expect(stack.pop()).toBeUndefined();
        expect(stack.size).toBe(0);
    });

    it("should find items in stack", () => {
        var stack = new Stack<number>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        expect(stack.find(2)?.value).toBe(2);
        expect(stack.find(4)).toBeUndefined();
    });

    it("should iterate over stack", () => {
        var stack = new Stack<number>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        var items = [];
        for (let item of stack) {
            items.push(item);
        }
        expect(items).toEqual([3, 2, 1]);
    });

    it("should convert stack to list", () => {
        var stack = new Stack<number>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        expect(stack.toList()).toEqual([3, 2, 1]);
    });
});
