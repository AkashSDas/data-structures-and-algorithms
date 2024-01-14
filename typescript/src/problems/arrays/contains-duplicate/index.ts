// Best solution
//
// Use set data structure.
// Time complexity - O(n)
// Space complexity - O(n)
export function containsDuplicate(nums: number[]): boolean {
    var set = new Set();

    for (let num of nums) {
        if (set.has(num)) {
            return true;
        } else {
            set.add(num);
        }
    }

    return false;
}

// Sort the list first and then loop over the list and compare previous element
// with current one to check if we've duplicates as in sorted list duplicates
// are adjacent to each other.
//
// Time complexity - O(nlogn) (sorting)
// Space complexity - O(1) (sorting can take some space)
function containsDuplicate2(nums: number[]): boolean {
    nums = nums.sort();
    var prev = 0;

    if (nums.length <= 1) return false;

    for (let idx = 1; idx < nums.length; idx++) {
        if (nums[idx] == prev) {
            return true;
        }
    }

    return false;
}

// Worst solution
//
// Looping through the list with current item and then doing a internal loop to
// check if that item is present in the list or not.
//
// Time complexity - O(n^2)
// Space complexity - O(1)
function containsDuplicate3(nums: number[]): boolean {
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (i != j && nums[i] == nums[j]) {
                return true;
            }
        }
    }

    return false;
}
