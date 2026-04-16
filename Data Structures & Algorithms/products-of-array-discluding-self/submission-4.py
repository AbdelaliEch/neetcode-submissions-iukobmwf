class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product_with_zero = product_without_zero = 1
        for num in nums:
            product_with_zero *= num
            if num != 0:
                product_without_zero *= num
        zeros_count = nums.count(0)

        if zeros_count > 1:
            return [0] * len(nums)

        for num in nums:
            if zeros_count == 1:
                result.append(0 if num != 0 else product_without_zero)
            else:
                result.append(product_without_zero//num if num != 0 else 0)
        return result


