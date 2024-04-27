/**
 * space complexity -- O(n)
 * time complexity -- O(n)
 */
export function longestConsecutive(nums: number[]): number {
    const uniqueNums = new Set(nums);
    let longestSequence = 0;
    let currentLength = 0;

    for (const num of Array.from(uniqueNums)) {
        const prevNum = num - 1; // check if its the starting num in a sequence

        if (currentLength > longestSequence) {
            longestSequence = currentLength;
        }

        // Starting a sequence
        if (!uniqueNums.has(prevNum)) {
            currentLength = 1;
            let nextNum = num + 1;

            while (uniqueNums.has(nextNum)) {
                currentLength++;
                nextNum++;
            }

            if (currentLength > longestSequence) {
                longestSequence = currentLength;
            }
        }
    }

    return longestSequence;
}
