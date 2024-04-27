/**
 * time complexity -- O(n)
 * space complexity -- O(n) -- in worst case all numbers will be unique and the nested
 * loop will be looped once only hence O(1) for the nested loop and overall O(n) (2 for loops)
 */
export function topKFrequent(nums: number[], k: number): number[] {
    const counts: Record<number, number> = {};
    for (let i = 0; i < nums.length; i++) {
        counts[nums[i]] = (counts[nums[i]] ?? 0) + 1;
    }

    const occurance: string[][] = Array(nums.length);
    for (const key in counts) {
        const count = counts[key];

        if (occurance[count] !== undefined) {
            occurance[count].push(key);
        } else {
            occurance[count] = [key];
        }
    }

    const kNums: number[] = [];
    for (let i = occurance.length - 1; i >= 0; i--) {
        const numsAtI = occurance[i];

        if (numsAtI !== undefined) {
            for (let j = 0; j < numsAtI.length; j++) {
                kNums.push(Number(numsAtI[j]));
                if (kNums.length === k) break;
            }
        }

        if (kNums.length === k) break;
    }

    return kNums;
}
