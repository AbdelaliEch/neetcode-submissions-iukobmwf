class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_pref = [1] * len(nums)
        prod_suff = [1] * len(nums)

        for i in range(1, len(nums)):
            prod_pref[i] = prod_pref[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            prod_suff[i] = prod_suff[i + 1] * nums[i + 1]

        output = [prod_pref[i] * prod_suff[i] for i in range(len(nums))]
        
        return output

# [1,2,4,6]
# [1,1,2,8] [48,24,6,1]

