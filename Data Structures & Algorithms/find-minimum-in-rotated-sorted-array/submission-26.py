class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            # mid is in right sorted half, so min can't be in front of mid, min is mid or behind mid
            if nums[mid] < nums[right]:
                right = mid
            # mid is in left sorted half
            else:
                left = mid + 1
        print(left, mid, right)
        return nums[mid]
        
        