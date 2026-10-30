class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums) 

        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_product[i] *= suffix_product
            suffix_product *= nums[i]
        return prefix_product

# time: O(n)
# space: O(n)

# [1,2,4,6]

# [1,1,2,8] 48 = [48 , 24, 12, 8]