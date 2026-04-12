class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        if nums[0] == target:
            return 0
        while i <= j:
            middle = (i + j) // 2
            if target < nums[middle]:
                j = middle - 1
            elif target > nums[middle]:
                i = middle + 1
            else:
                return middle
        return -1   