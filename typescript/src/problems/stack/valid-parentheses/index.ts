function isValid(s: string): boolean {
    var brackets: Record<string, string> = {
        "}": "{",
        ")": "(",
        "]": "[",
    };

    var closingBrackets = new Set(Object.keys(brackets));
    var stack: string[] = [];

    for (let i = 0; i < s.length; i++) {
        let bracket = s[i];

        if (!closingBrackets.has(bracket)) {
            stack.push(bracket);
        } else {
            let lastBracket = stack.pop();

            if (lastBracket == undefined || lastBracket != brackets[bracket]) {
                return false;
            }
        }
    }

    return stack.length == 0;
}
