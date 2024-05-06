function searchInRotated(nums: number[], target: number): number {
    let start = 0;
    let end = nums.length - 1;

    while (start <= end) {
        const mid = start + Math.floor((end - start) / 2);
        const elementAtMid = nums[mid];

        if (elementAtMid === target) {
            return mid;
        }

        if (nums[start] <= elementAtMid) {
            // left sorted region

            if (target > elementAtMid || target < nums[start]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        } else {
            // right sorted region

            if (target < elementAtMid || target > nums[end]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
    }

    return -1;
}
