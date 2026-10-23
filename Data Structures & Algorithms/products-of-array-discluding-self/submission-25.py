class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        current_suffix_product = 1

        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= current_suffix_product
            current_suffix_product *= nums[i]
        return output

# time: O(n)
# space: O(1)

# [1 2 4 6]
# [1 1 2 8] [48 24 6 1]
# [48 24 12 8]