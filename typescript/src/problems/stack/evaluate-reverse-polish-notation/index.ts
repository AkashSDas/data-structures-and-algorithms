type Operand = "+" | "-" | "*" | "/";
const operands = new Set<Operand>(["+", "-", "/", "*"]);

function performOperation(x: number, y: number, operand: Operand): number {
    switch (operand) {
        case "+":
            return x + y;
        case "-":
            return x - y;
        case "*":
            return x * y;
        case "/": {
            const result = x / y;
            if (result < 0) {
                return Math.ceil(result);
            } else {
                return Math.floor(result);
            }
        }
        default:
            throw new Error("Invalid operand");
    }
}

function evalRPN(tokens: string[]): number {
    const stack: number[] = [];

    for (const token of tokens) {
        if (!operands.has(token as any)) {
            stack.push(parseInt(token, 10));
        } else {
            const y = stack.pop()!;
            const x = stack.pop()!;
            const result = performOperation(x, y, token as Operand);
            stack.push(result);
        }
    }

    return stack.pop() ?? NaN;
}
