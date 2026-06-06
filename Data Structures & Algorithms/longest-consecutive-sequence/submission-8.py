class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s_nums = sorted(set(nums))
        print(s_nums)
        max_count = 1
        i = 1
        while i < len(s_nums):
            count = 1
            while i < len(s_nums) and s_nums[i] == s_nums[i - 1] + 1:
                print(i)
                count += 1
                i += 1
            max_count = max(count, max_count)
            i += 1
        return max_count