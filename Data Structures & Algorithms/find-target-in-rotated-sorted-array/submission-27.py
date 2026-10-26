class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # k = 0
        while left <= right:
            # print(left, right)
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target == nums[right]:
                return right
            elif target == nums[left]:
                return left
            
            # middle is in the right sorted half
            if nums[middle] < nums[right]:
                if nums[middle] < target < nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # middle is in the left sorted half
            else:
                if nums[left] < target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

        # print(left, middle, right)
        return -1

# we need some if statements to determine where the target is, to the right or to the left 