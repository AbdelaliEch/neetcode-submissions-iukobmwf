class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            # print(nums[left], nums[middle], nums[right], nums[left:right+1])

            if target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            elif target == nums[middle]:
                return middle


            # middle is in right sorted half
            if nums[middle] < nums[right]:
                if nums[middle] < target < nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # middle is in left sorted half
            else:
                if nums[left] < target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        # print(nums[left], nums[middle], nums[right], nums[left:right+1])
        return -1