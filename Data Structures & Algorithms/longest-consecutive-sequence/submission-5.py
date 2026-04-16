class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums) # O(n)
        
        visited = set()

        count = 0
        max_count = 0
        
        for num in nums_set:
            if num not in visited:
                num2 = num
                while num2 in nums_set:
                    visited.add(num2)
                    num2 += 1
                    count += 1
                max_count = max(count, max_count)
            count = 0
        return max_count
            


            
                