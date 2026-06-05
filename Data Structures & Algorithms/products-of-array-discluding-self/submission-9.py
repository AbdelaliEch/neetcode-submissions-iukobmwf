class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)


        total, total_without_zero = 1, 1
        for num in nums:
            total *= num
            if num != 0:
                total_without_zero *= num
        
        for num in nums:
            if num != 0:
                output.append(total // num)
            else:
                output.append(total_without_zero)
            
        
        return output