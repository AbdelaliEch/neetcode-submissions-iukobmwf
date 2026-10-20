class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        zero_count = nums.count(0)

        if zero_count == 1:
            product = 1
            for num in nums:
                if num == 0:
                    continue
                product *= num
            output[nums.index(0)] = product
        elif zero_count == 0:
            product = 1
            for num in nums:
                product *= num
            for i in range(len(nums)):
                output[i] = product // nums[i]
        return output

# [1 2 3 4] = [26 12 8 6] 
# [1 2 3 0] = [0 0 0 6]
# [1 2 3 0 0] = [0 0 0 0 0]