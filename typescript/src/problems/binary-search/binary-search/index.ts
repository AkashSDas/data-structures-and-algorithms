/**
 * time complexity -- O(logn)
 * space complexity -- O(1)
 */
function search(nums: number[], target: number): number {
    let startIdx = 0;
    let endIdx = nums.length - 1;

    while (startIdx <= endIdx) {
        const midIdx = startIdx + Math.floor((endIdx - startIdx) / 2);
        const elementAtMid = nums[midIdx];

        if (elementAtMid === target) {
            return midIdx;
        } else if (target < elementAtMid) {
            endIdx = midIdx - 1;
        } else {
            startIdx = midIdx + 1;
        }
    }

    return -1;
}

// console.log(search([-1, 0, 3, 5, 9, 12], 9));
