class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        output = []

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            output.append(prefix_product[i] * suffix_product[i])
        return output


# [1 2 4 6]
# [1 1 2 8] [48 24 6 1]
# [48 24 12 8]