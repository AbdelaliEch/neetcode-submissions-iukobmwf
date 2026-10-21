class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_count = 1
        mins_set = set()

        for num in nums:
            if num - 1 not in nums_set and num not in mins_set:
                mins_set.add(num)

        for min_num in mins_set:
            current_min = min_num
            count = 1
            while current_min + 1 in nums_set:
                count += 1
                current_min += 1
            max_count = max(count, max_count)
            print(max_count)
        
        return max_count

# time: O(n) + O(n)
# space: O(n)