type Operand = "+" | "-" | "*" | "/";

function performOperation(x: number, y: number, operand: Operand): number {
    switch (operand) {
        case "+":
            return x + y;
        case "-":
            return x - y;
        case "*":
            return x * y;
        case "/":
            let result = x / y;
            if (result < 0) {
                return Math.ceil(result);
            } else {
                return Math.floor(result);
            }
    }
}

var operands = new Set<Operand>(["+", "-", "/", "*"]);

function evalRPN(tokens: string[]): number {
    var stack: string[] = [];

    for (let i = 0; i < tokens.length; i++) {
        let token = tokens[i];

        if (operands.has(token as any)) {
            let y = parseInt(stack.pop() ?? "0");
            let x = parseInt(stack.pop() ?? "0");
            let result = performOperation(x, y, token as any);
            stack.push(String(result));
        } else {
            stack.push(token);
        }
    }

    return parseInt(stack.pop() ?? "0");
}

console.log(evalRPN(["2", "1", "+", "3", "*"]));
