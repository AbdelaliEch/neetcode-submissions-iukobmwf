class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        d_nums = set(nums)

        for num in d_nums:
            # it means it is a start of a sequence
            if num - 1 not in d_nums:
                count = 1
                while num + count in d_nums:
                    count += 1
                max_count = max(count, max_count)

        return max_count

# complexity: O(n) O(n)

