function longestConsecutive(nums: number[]): number {
    var uniqueNums = new Set(nums);
    var longestSequence = 0;
    var currentLength = 0;

    for (let num of Array.from(uniqueNums)) {
        let previousNum = num - 1; // check if its the starting num in a sequence

        // Starting a sequence
        if (!uniqueNums.has(previousNum)) {
            if (currentLength > longestSequence) {
                longestSequence = currentLength;
            }
            currentLength = 1;

            let nextNum = num + 1;
            while (uniqueNums.has(nextNum)) {
                currentLength++;
                nextNum = nextNum + 1;
            }

            if (currentLength > longestSequence) {
                longestSequence = currentLength;
            }
        }
    }

    return longestSequence;
}

function longestConsecutive2(nums: number[]): number {
    if (nums.length == 0) return 0;

    var max = Math.max(...nums);
    var min = Math.max(...nums);
    var positiveSequence: number[] = Array(max + 1); // +1 is for number 0, for positive nums starting from 0
    var negativeSequence: number[] = Array(Math.abs(min)); // for negative nums

    // Putting num in sequence at index num
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];

        if (num < 0) {
            negativeSequence[Math.abs(num)] = nums[i];
        } else {
            positiveSequence[num] = nums[i];
        }
    }

    var longestSequence = 0;
    var currentLength = 0;

    // not equal to zero because we'll only have nums -1 (from -Infinity) not 0
    for (let i = negativeSequence.length - 1; i > 0; i--) {
        let item = negativeSequence[i];

        if (item == undefined) {
            if (currentLength > longestSequence) {
                longestSequence = currentLength;
            }
            currentLength = 0;
        } else {
            currentLength++;
        }
    }

    for (let i = 0; i < positiveSequence.length; i++) {
        let item = positiveSequence[i];

        if (item == undefined) {
            if (currentLength > longestSequence) {
                longestSequence = currentLength;
            }
            currentLength = 0;
        } else {
            currentLength++;
        }
    }

    // incase no item is undefined
    if (currentLength > longestSequence) {
        longestSequence = currentLength;
    }

    return longestSequence;
}

// console.log(longestConsecutive([-2, -1, 1]));
// console.log(
//     longestConsecutive([
//         4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3,
//     ])
// );

// console.log(
//     longestConsecutive([
//         0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999,
//     ])
// );

console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));
