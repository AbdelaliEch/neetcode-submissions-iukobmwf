class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        if nums[0] == target:
            return 0
        while i < j:
            middle = (i + j) // 2
            if middle in (i, j):
                if target not in (nums[i], nums[j]):
                    return -1
                if target == nums[i]:
                    return i
                if target == nums[j]:
                    return j

            if target < nums[middle]:
                j = middle
            elif target > nums[middle]:
                i = middle
            else:
                return middle
        return -1   