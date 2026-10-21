class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        # nums_min = min(nums)
        # current_min = nums_set[0]
        count = max_count = 1
        mins_list = []

        for num in nums:
            if num - 1 not in nums_set:
                mins_list.append(num)
        print(mins_list)
        for min_num in mins_list:
            current_min = min_num
            count = 1
            while current_min + 1 in nums_set:
                count += 1
                current_min += 1
            max_count = max(count, max_count)
            print(max_count)
        
        return max_count

# we should find the start of the sequence, which is the min
# start of the sequence, min that has no number below it by 1
# end of the sequence, max that has no number above it by 1

# [20,0,2,10,3,4,5], min here is 0, max is 20

# O(n) means we will traverse the array once

# current min
# we can use a set so we can search with O(1)