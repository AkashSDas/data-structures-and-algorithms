class MinStack {
    private min: number | undefined;
    stack: { val: number; min: number | undefined }[];

    constructor() {
        this.stack = [];
        this.min = undefined;
    }

    push(val: number): void {
        if (this.min == undefined || val < this.min) {
            this.stack.push({ val, min: val });
            this.min = val;
        } else {
            this.stack.push({ val, min: this.min });
        }
    }

    pop(): void {
        var result = this.stack.pop();

        if (result != undefined && result.min == this.min) {
            if (this.stack.length > 0) {
                this.min = this.stack[this.stack.length - 1].min;
            } else {
                this.min = undefined;
            }
        }
    }

    top(): number {
        return this.stack[this.stack.length - 1].val;
    }

    getMin(): number {
        return this.stack[this.stack.length - 1].min ?? NaN;
    }
}

// ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
// [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
// [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
// [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]

// 2147483646
// 2147483647

var stack = new MinStack();
stack.push(2147483646);
stack.push(2147483646);
stack.push(2147483647);
stack.pop();
stack.pop();
stack.pop();
stack.push(2147483647);

console.log(stack.getMin());
