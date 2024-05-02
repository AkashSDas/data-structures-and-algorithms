function findMin(nums: number[]): number {
    let startIdx = 0;
    let endIdx = nums.length - 1;
    let minVal = nums[0];

    while (startIdx <= endIdx) {
        if (nums[startIdx] < nums[endIdx]) {
            minVal = Math.min(minVal, nums[startIdx]);
            break;
        }

        const mid = Math.floor((startIdx + endIdx) / 2);
        const elementAtMid = nums[mid];

        if (minVal > elementAtMid) {
            minVal = elementAtMid;
        }

        if (elementAtMid >= nums[startIdx]) {
            startIdx = mid + 1;
        } else {
            endIdx = mid - 1;
        }
    }

    return minVal;
}
