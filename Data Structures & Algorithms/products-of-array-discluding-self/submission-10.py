class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        product, zero_count = 1, nums.count(0)
        
        if zero_count > 1:
            return output

        for num in nums:
            if num != 0:
                product *= num
        
        for i, num in enumerate(nums):
            if zero_count == 1:
                output[i] = 0 if num != 0 else product
            else:
                output[i] = product // num
            
        return output