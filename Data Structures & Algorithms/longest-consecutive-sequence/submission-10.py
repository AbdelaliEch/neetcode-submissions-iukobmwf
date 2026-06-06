class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        d_nums = set(nums)
        starts = {num for num in d_nums if num - 1 not in d_nums}

        for start in starts:
            current_min = start
            count = 1
            while current_min + 1 in d_nums:
                current_min += 1
                count += 1
            max_count = max(count, max_count)

        return max_count

