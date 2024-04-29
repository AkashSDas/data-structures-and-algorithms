export function threeSum(nums: number[]): number[][] {
    const results: number[][] = [];
    // The sort() method in JavaScript (and TypeScript) sorts elements as strings by default, which can lead to unexpected results when sorting numbers.
    nums.sort((a, b) => a - b); // Sort the nums array in ascending order

    for (let i = 0; i < nums.length; i++) {
        // if num is equal to previous num then we've already calculated whether its
        // triple or not. So skipping it. This also helps us to prevent duplicate triplet
        // creation.
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let j = i + 1;
        let k = nums.length - 1;

        while (j < k) {
            const sum = nums[i] + nums[j] + nums[k];
            if (sum > 0) {
                k--;
            } else if (sum < 0) {
                j++;
            } else {
                results.push([nums[i], nums[j], nums[k]]);
                j++;

                while (nums[j] === nums[j - 1] && j < k) {
                    j++;
                }
            }
        }
    }

    return results;
}

/**
 * Time Limit Exceeded
 * space complexity -- O(n)
 * time complexity -- O(n^3)
 */
export function threeSum2(nums: number[]): number[][] {
    const results: number[][] = [];
    const solutionKey = new Set<string>();

    for (let i = 0; i < nums.length; i++) {
        const elementAtI = nums[i];

        for (let j = i + 1; j < nums.length; j++) {
            const elementAtJ = nums[j];
            let k = nums.length - 1;

            while (j < k) {
                const elementAtK = nums[k];

                if (
                    elementAtI + elementAtJ + elementAtK === 0 &&
                    i !== j &&
                    j !== k &&
                    i !== k &&
                    !solutionKey.has(
                        [elementAtI, elementAtJ, elementAtK].sort().toString()
                    )
                ) {
                    results.push([elementAtI, elementAtJ, elementAtK].sort());
                    solutionKey.add(
                        [elementAtI, elementAtJ, elementAtK].sort().toString()
                    );
                }

                k--;
            }
        }
    }

    return results;
}

// console.log(threeSum([-1, 0, 1, 2, -1, -4]));
