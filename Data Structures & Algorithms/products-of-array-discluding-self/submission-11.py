class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums) 
        suff = [1] * len(nums)

        for i in range(len(nums)):
            pref[i] = pref[i - 1] * nums[i] if i > 0 else nums[i]

        for j in range(len(nums) - 1, -1, -1):
            suff[j] = suff[j + 1] * nums[j] if j < len(nums) - 1 else nums[j]

        # print(pref, suff) 

        output = []
        for i, num in enumerate(nums):
            if i == 0:
                output.append(suff[i + 1])
            elif i == len(nums) - 1:
                output.append(pref[i - 1])
            else:
                output.append(pref[i - 1] * suff[i + 1])

        # print(output)
        return output



