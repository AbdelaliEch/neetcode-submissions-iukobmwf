class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                seq_num = num
                count = 1
                while seq_num + 1 in nums_set:
                    seq_num += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count

# time: O(n)
# space: O(n)