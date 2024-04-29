// uses 2 pointer approach
// space complexity -- O(1)
// time complexity -- O(n)
function trap(height: number[]): number {
    let i = 0;
    let j = height.length - 1;
    let maxOnLeftSide = height[i];
    let maxOnRightSide = height[j];
    let capacity = 0;

    while (i < j) {
        if (maxOnLeftSide < maxOnRightSide) {
            i++;
            maxOnLeftSide = Math.max(height[i], maxOnLeftSide);
            capacity += maxOnLeftSide - height[i];
        } else {
            j--;
            maxOnRightSide = Math.max(height[j], maxOnRightSide);
            capacity += maxOnRightSide - height[j];
        }
    }

    return capacity;
}

// space complexity -- O(n)
// time complexity -- O(n)
function trap1(height: number[]): number {
    let capacity = 0;

    for (let i = 0; i < height.length; i++) {
        let maxOnLeftSide = Math.max(...height.slice(0, i));
        let maxOnRightSide = Math.max(...height.slice(i + 1));
        const minOfLeftAndRight = Math.min(maxOnLeftSide, maxOnRightSide);
        capacity += Math.max(0, minOfLeftAndRight - height[i]);
    }

    return capacity;
}

console.log(trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));

// Overall space and time complexities are O(1) and O(n^2) respectively. Time limit exceeded

// amount of water stored at height i
function findWaterCapacityAtBlock2(height: number[], idx: number): number {
    let i = idx - 1;
    let j = idx + 1;
    let maxAtLeftSide = 0;
    let maxAtRightSide = 0;

    while (i >= 0 || j <= height.length - 1) {
        if (idx !== 0 && height[i] > maxAtLeftSide) {
            maxAtLeftSide = height[i];
        }

        if (idx !== height.length - 1 && height[j] > maxAtRightSide) {
            maxAtRightSide = height[j];
        }

        if (i > -1) i--;
        if (j < height.length + 1) j++;
    }

    let capacity = 0;
    if (height[idx] < maxAtLeftSide && height[idx] < maxAtRightSide) {
        capacity = Math.min(maxAtLeftSide, maxAtRightSide);
    }
    return Math.max(0, capacity - height[idx]);
}

function trap2(height: number[]): number {
    let capacity = 0;

    for (let i = 0; i < height.length; i++) {
        capacity += findWaterCapacityAtBlock2(height, i);
    }

    return capacity;
}
