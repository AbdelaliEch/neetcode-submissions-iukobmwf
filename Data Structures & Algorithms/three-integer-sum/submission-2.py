class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            while i < j:
                if i == k:
                    i+=1
                    continue
                if j==k:
                    j-=1
                    continue

                if nums[i] + nums[j] > -nums[k]:
                    j -=1
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    if not ((i > 0 and not nums[i] != nums[i - 1]) and (j < len(nums) - 1 and not nums[j] != nums[j + 1])):
                        result.append([nums[k] , nums[i], nums[j]])
                    i+=1
                    j-=1
        return result
                    
# [-4, -1, -1, 0, 1, 2]