/**
 * time complexity -- O(n)
 * space complexity -- O(n)
 */
function largestRectangleArea(heights: number[]): number {
    const stack: [number, number][] = []; // [idx,height][]
    let maxArea = 0;

    for (let i = 0; i < heights.length; i++) {
        const currHeight = heights[i];

        let newIdx = i;
        while (stack.length > 0 && stack[stack.length - 1][1] > currHeight) {
            const [idx, height] = stack.pop()!;
            maxArea = Math.max(maxArea, height * (i - idx));
            newIdx = idx;
        }

        stack.push([newIdx, currHeight]);
    }

    while (stack.length > 0) {
        const [idx, height] = stack.pop()!;
        maxArea = Math.max(maxArea, height * (heights.length - idx));
    }

    return maxArea;
}

/**
 * time complexity -- O(n^2)
 * space complexity -- O(n)
 */
function largestRectangleArea2(heights: number[]): number {
    let maxArea = 0;

    for (let i = 0; i < heights.length; i++) {
        // area of bar at i itself
        const areas: number[] = [heights[i]];

        for (let j = i + 1; j < heights.length; j++) {
            const minHeight = Math.min(...heights.slice(i, j + 1));
            areas.push(minHeight * (j - i + 1));
        }

        if (maxArea < Math.max(...areas)) {
            maxArea = Math.max(...areas);
        }
    }

    return maxArea;
}
