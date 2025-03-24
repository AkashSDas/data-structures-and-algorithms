class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        curr_len = 0
        max_len = 0

        for num in list(unique_nums):
            prev_num = num - 1

            if curr_len > max_len:
                max_len = curr_len

            if prev_num not in unique_nums:
                curr_len = 1
                next_num = num + 1

                while next_num in unique_nums:
                    curr_len += 1
                    next_num += 1

                if curr_len > max_len:
                    max_len = curr_len

        return max_len
