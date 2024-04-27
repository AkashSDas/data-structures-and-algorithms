/**
 * space complexity -- O(1)
 * time complexity -- O(n)
 */
export function twoSum(nums: number[], target: number): [number, number] {
    let leftIdx = 0;
    let rightIdx = nums.length - 1;

    while (leftIdx < rightIdx) {
        if (nums[leftIdx] + nums[rightIdx] > target) {
            rightIdx--;
        } else if (nums[leftIdx] + nums[rightIdx] < target) {
            leftIdx++;
        } else {
            return [++leftIdx, ++rightIdx];
        }
    }

    return [NaN, NaN];
}
