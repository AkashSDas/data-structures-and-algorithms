from typing import List

number = int | float


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists: set[number] = set()

        for num in nums:
            if num in exists:
                return True
            else:
                exists.add(num)

        return False


# Best solution
#
# time complexity -- O(n)
# space complexity -- O(n)
def contains_duplicate(nums: list[number]) -> bool:
    exists: set[number] = set()

    for num in nums:
        if num in exists:
            return True
        else:
            exists.add(num)

    return False


# Worst solution
#
# time complexity -- O(n^2)
# space complexity -- O(1)
def contains_duplicate_2(nums: list[number]) -> bool:
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] == nums[j] and i != j:
                return True

    return False


# Sort the list first and then loop over the list and compare previous element
# with current one to check if we've duplicates as in sorted list duplicates
# are adjacent to each other.
#
# time complexity -- O(nlogn) (sorting)
# space complexity -- O(1) (but sorting can take some space)
def contains_duplicate_3(nums: list[number]) -> bool:
    if len(nums) <= 1:
        return False

    nums.sort()
    prev_idx = 0

    for curr_idx in range(1, len(nums)):
        if nums[prev_idx] == nums[curr_idx]:
            return True

        prev_idx += 1

    return False
