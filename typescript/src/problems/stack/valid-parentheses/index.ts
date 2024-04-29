const brackets: Record<string, string> = {
    "}": "{",
    ")": "(",
    "]": "[",
};

function isValid(s: string): boolean {
    const stack: string[] = [];

    for (const bracket of s) {
        const isOpening = Object.values(brackets).includes(bracket);
        if (isOpening) {
            stack.push(bracket);
        } else {
            const lastBracket = stack.pop();
            if (lastBracket !== brackets[bracket]) {
                return false;
            }
        }
    }

    if (stack.length !== 0) {
        return false;
    }

    return true;
}
