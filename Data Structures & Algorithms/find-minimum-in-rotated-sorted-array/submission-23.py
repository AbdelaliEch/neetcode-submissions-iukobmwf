class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            print(nums[left], nums[middle], nums[right], nums[left:right+1])

            # middle is in the right sorted half, so the min can't be in front of the middle
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        # print(nums[left], nums[middle], nums[right], nums[left:right+1])
        return nums[middle]

