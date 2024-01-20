// only add open parenthese if open < n
// only add close parenthese if close < open
// valid if open == close == n

function generateParenthesis(n: number): string[] {
    var result: string[] = [];
    var stack: string[] = [];

    backTracking(0, 0);
    return result;

    function backTracking(openCount: number, closeCount: number) {
        if (openCount == closeCount && closeCount == n) {
            result.push(stack.join(""));
            return;
        }

        if (openCount < n) {
            stack.push("(");
            backTracking(openCount + 1, closeCount);
            stack.pop();
        }

        if (closeCount < openCount) {
            stack.push(")");
            backTracking(openCount, closeCount + 1);
            stack.pop();
        }
    }
}
