class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)

        prod = 1
        for num in nums:
            if num != 0:
                prod *= num

        for num in nums:
            if zero_count == 1:
                res.append(prod if num == 0 else 0)
            else:
               res.append(prod // num) 

        return res

# [1,2,4,6] = [48,24,12,8]
# [-1,0,1,2,3] = [0,-6,0,0,0]
# [-1,0,1,2,0] = [0,0,0,0,0,0]