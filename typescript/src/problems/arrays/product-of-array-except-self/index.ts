/**
 * time complexity -- O(n)
 * space complexity -- O(n)
 */
export function productExceptSelf(nums: number[]): number[] {
    if (nums.length <= 1) return nums;
    const results = Array<number>(nums.length);

    let prefix = 1;
    for (let i = 0; i < nums.length; i++) {
        if (i === 0) {
            results[i] = 1;
        } else {
            results[i] = prefix;
        }

        prefix *= nums[i];
    }

    let postfix = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        if (i === nums.length - 1) {
            results[i] = results[i];
        } else {
            results[i] = postfix * results[i];
        }

        postfix *= nums[i];
    }

    return results;
}

/**
 * time complexity -- O(n^2)
 * space complexity -- O(n)
 */
export function productExceptSelf2(nums: number[]): number[] {
    if (nums.length <= 1) return nums;

    const results = Array<number>(nums.length);

    for (let i = 0; i < nums.length; i++) {
        let product = 1;

        for (let j = 0; j < nums.length; j++) {
            if (i !== j) {
                product *= nums[j];
            }
        }

        results[i] = product;
    }

    return results;
}
