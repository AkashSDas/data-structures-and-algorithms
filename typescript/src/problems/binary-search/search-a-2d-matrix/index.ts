function searchAtRow(nums: number[], target: number): number {
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

function searchMatrix(matrix: number[][], target: number): boolean {
    let startIdx = 0;
    let endIdx = matrix.length - 1;

    while (startIdx <= endIdx) {
        const midIdx = startIdx + Math.floor((endIdx - startIdx) / 2);
        const midRow = matrix[midIdx];

        if (target >= midRow[0] && target <= midRow[midRow.length - 1]) {
            const result = searchAtRow(midRow, target);
            if (result === -1) return false;
            else return true;
        } else if (target < midRow[0] && target < midRow[midRow.length - 1]) {
            endIdx = midIdx - 1;
        } else {
            startIdx = midIdx + 1;
        }
    }

    return false;
}
