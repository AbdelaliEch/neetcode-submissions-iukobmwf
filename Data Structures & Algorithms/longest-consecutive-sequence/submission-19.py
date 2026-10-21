class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_count = 1
        mins_list = []

        for num in nums:
            if num - 1 not in nums_set:
                mins_list.append(num)
        for min_num in mins_list:
            current_min = min_num
            count = 1
            while current_min + 1 in nums_set:
                count += 1
                current_min += 1
            max_count = max(count, max_count)
            print(max_count)
        
        return max_count

# time: O()
# space: O()