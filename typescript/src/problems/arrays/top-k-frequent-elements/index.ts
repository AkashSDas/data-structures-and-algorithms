function topKFrequent(nums: number[], k: number): number[] {
    if (k === 0) return [];
    var counts: Record<number, number> = {};

    for (let i = 0; i < nums.length; i++) {
        counts[nums[i]] = (counts[nums[i]] ?? 0) + 1;
    }

    var occurrence = Array(nums.length);
    for (let key in counts) {
        let count = counts[key];

        if (occurrence[count] == undefined) {
            occurrence[count] = [key];
        } else {
            occurrence[count].push(key);
        }
    }

    var kNums: number[] = [];
    for (let i = nums.length; i >= 0; i--) {
        let numsAtI = occurrence[i];

        if (numsAtI != undefined) {
            for (let j = 0; j < numsAtI.length; j++) {
                kNums.push(Number(numsAtI[j]));
                if (kNums.length === k) break;
            }
        }

        if (kNums.length === k) break;
    }

    return kNums;
}

console.log(topKFrequent([1], 1));
