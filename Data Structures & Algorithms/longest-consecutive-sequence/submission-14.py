class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        max_count = count = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
        max_count = max(count, max_count)
        print(nums, count, max_count)
        return max_count

# we should find the start of the sequence, which is the min