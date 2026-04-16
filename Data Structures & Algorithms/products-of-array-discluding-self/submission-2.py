class Solution:
    def is_all_zero(self, nums):
        for num in nums:
            if num != 0:
                return False
        return True
    
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if self.is_all_zero(nums):
            return nums

        result = []
        product_with_zero = product_without_zero = 1
        for num in nums:
            product_with_zero *= num
            if num != 0:
                product_without_zero *= num
        # product_with_zero = abs(product_with_zero)
        # product_without_zero = abs(product_without_zero)
        zeros_count = nums.count(0)
        if zeros_count > 1:
            return [0] * len(nums)

        for num in nums:
            if zeros_count == 1:
                result.append(0 if num != 0 else product_without_zero)
            # elif zeros_count > 1:
            #     result.append(0)
            else:
                result.append(product_without_zero//num if num != 0 else 0)
        return result


