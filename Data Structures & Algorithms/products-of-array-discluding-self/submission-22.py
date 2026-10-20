class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        prefix_product = [0] * n
        suffix_product = [0] * n

        prefix_product[0] = suffix_product[-1] = 1

        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        for i in range(0, n):
            output[i] = prefix_product[i] * suffix_product[i]
        return output

# [1 2 4 6] = [1 1 2 8] | [48 24 6 1] = [48 24 12 8] 
# time: O(n)
# space: O(n)