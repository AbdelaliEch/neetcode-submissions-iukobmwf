class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        while l + 1 < r:
            middle = (l + r) // 2
            if nums[middle] > nums[l] and nums[middle] < nums[r]:
                # go left
                r = middle
            elif nums[middle] > nums[l] and nums[middle] > nums[r]:
                # go right
                l = middle
            elif nums[middle] < nums[l] and nums[middle] < nums[r]:
                # go left
                r = middle
        return min(nums[l], nums[r])

    

