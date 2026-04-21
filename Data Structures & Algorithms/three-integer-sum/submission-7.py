class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for k in range(len(nums)):
            # it means the nums[k] and nums[i] and nums[j] will be positive, so they cannot form a combination
            # because a combination needs at least a 0 or a negative numbers
            # and i and j are always above k
            if nums[k] > 0: 
                break;
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] > -nums[k]:
                    j -=1
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    result.append([nums[k] , nums[i], nums[j]])
                    i+=1
                    j-=1
                    while nums[i] == nums[i - 1] and i < j:
                        i+=1

        return result
                    