class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_count = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                current_min = num
                count = 1
                while current_min + 1 in nums_set:
                    count += 1
                    current_min += 1
                max_count = max(count, max_count)            
        
        return max_count

# time: O(n)
# space: O(n)