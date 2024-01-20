function dailyTemperatures(temperatures: number[]): number[] {
    var results: number[] = Array(temperatures.length).fill(0);
    var stack: [number, number][] = []; // [temp, idx]

    for (let i = 0; i < temperatures.length; i++) {
        let currTemp = temperatures[i];

        while (stack.length > 0 && currTemp > stack[stack.length - 1][0]) {
            let result = stack.pop()!;
            results[result[1]] = i - result[1];
        }

        stack.push([currTemp, i]);
    }

    return results;
}

function dailyTemperatures2(temperatures: number[]): number[] {
    var results: number[] = [];

    for (let i = 0; i < temperatures.length; i++) {
        let currTemp = temperatures[i];

        for (let j = i + 1; j < temperatures.length; j++) {
            let nextTemp = temperatures[j];

            if (nextTemp > currTemp) {
                results.push(j - i);
                break;
            }
        }

        // no date found
        if (results.length - 1 != i) {
            results.push(0);
        }
    }

    return results;
}
