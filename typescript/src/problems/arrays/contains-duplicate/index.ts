/**
 * Best solution
 *
 * time complexity -- O(n)
 * space complexity -- O(n)
 */
export function containsDuplicate(nums: number[]): boolean {
    const exists = new Set();

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (exists.has(num)) {
            return true;
        } else {
            exists.add(num);
        }
    }

    return false;
}

/**
 * Worst solution
 *
 * time complexity -- O(n^2)
 * space complexity -- O(1)
 */
export function containsDuplicate2(nums: number[]): boolean {
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[i] == nums[j] && i !== j) {
                return true;
            }
        }
    }

    return false;
}

/**
 * Sort the list first and then loop over the list and compare previous element
 * with current one to check if we've duplicates as in sorted list duplicates
 * are adjacent to each other.
 *
 * time complexity -- O(nlogn) (sorting)
 * space complexity -- O(1) (but sorting can take some space)
 */
export function containsDuplicate3(nums: number[]): boolean {
    if (nums.length <= 1) return false;

    nums.sort();
    const prev = 0;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[prev]) {
            return true;
        }
    }

    return false;
}
