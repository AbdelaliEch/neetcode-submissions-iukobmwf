class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix_product = [0] * len(nums)
        suffix_product = [0] * len(nums)

        prefix_product[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i]

        suffix_product[len(nums) - 1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]

        # print(prefix_product, suffix_product)

        output[0] = suffix_product[1]
        output[len(nums) - 1] = prefix_product[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            output[i] = prefix_product[i - 1] * suffix_product[i + 1]
        return output

# [1 2 4 6] = [48 24 12 8] 
# [1 2 8 48] [48 48 24 6] = [48 ]