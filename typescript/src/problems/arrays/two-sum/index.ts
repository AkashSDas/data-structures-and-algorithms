export function twoSum(nums: number[], target: number): number[] {
    var numWithPosition: Record<number, number> = {}; // num:idx

    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];

        if (numWithPosition[diff] != undefined) {
            return [i, numWithPosition[diff]];
        } else {
            numWithPosition[nums[i]] = i;
        }
    }

    return [NaN, NaN];
}

function twoSum1(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            }
        }
    }

    return [NaN, NaN];
}
