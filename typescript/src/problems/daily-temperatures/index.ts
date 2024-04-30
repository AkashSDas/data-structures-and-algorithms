/**
 * monotonic stack (stack with elements in decreasing order,
 * temperatures in stack will be in decreasing order).
 *
 * time complexity -- O(n)
 * space complexity -- O(n) -- result
 */
function dailyTemperatures(temperatures: number[]): number[] {
    const results = Array<number>(temperatures.length).fill(0);
    const stack: [number, number][] = []; // [item, idx][]

    for (let i = 0; i < temperatures.length; i++) {
        const currTemp = temperatures[i];

        while (stack.length > 0 && currTemp > stack[stack.length - 1][0]) {
            const result = stack.pop()!;
            results[result[1]] = i - result[1];
        }

        stack.push([currTemp, i]);
    }

    return results;
}

/**
 * time complexity -- O(n^2)  time limit exceeded
 * space complexity -- O(n) -- result
 */
function dailyTemperatures2(temperatures: number[]): number[] {
    const results = Array<number>(temperatures.length).fill(0);

    for (let i = 0; i < temperatures.length; i++) {
        const temperature = temperatures[i];
        let idx = i + 1;

        while (idx < temperatures.length) {
            if (temperatures[idx] > temperature) {
                results[i] = idx - i;
                break;
            }

            idx++;
        }
    }

    return results;
}
