class MinStack {
    private min: number | undefined;
    stack: { val: number; min: number | undefined }[];

    constructor() {
        this.stack = [];
        this.min = undefined;
    }

    push(val: number): void {
        if (this.min === undefined || val < this.min) {
            this.stack.push({ val, min: val });
            this.min = val;
        } else {
            this.stack.push({ val, min: this.min });
        }
    }

    pop(): void {
        const result = this.stack.pop();

        if (result !== undefined && result.min === this.min) {
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
