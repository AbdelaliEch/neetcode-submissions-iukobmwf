class Solution:



    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count = 0

        l = 0
        for r in range(len(nums)):
            # print(l, r, nums[l:r+1], count)
            while not (len(set(nums[l : r + 1])) == len(nums[l : r + 1]) and (sorted(nums[l : r + 1]) == nums[l :r + 1] or sorted(nums[l : r + 1], reverse=True) == nums[l : r + 1])):
                print(l, r, "invalid", nums[l:r+1], count)
                l += 1
            count = max(count, r - l + 1)
        # print("last list", nums[l:r+1], len(nums[l:r+1]))

        count = max(count, len(nums[l:r+1]))

        return count
            


# window is valid if sorted