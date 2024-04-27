/**
 * time complexity -- O(n)
 * space complexity -- O(n)
 */
export function twoSum(nums: number[], target: number): [number, number] {
    const numWithPosition: Record<number, number> = {}; // num:idx

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const diff = target - num;

        if (numWithPosition[diff] !== undefined) {
            return [i, numWithPosition[diff]];
        } else {
            numWithPosition[num] = i;
        }
    }

    return [NaN, NaN];
}
