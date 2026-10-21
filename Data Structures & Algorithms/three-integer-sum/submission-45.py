class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        output = []
        for i in range(len(nums)):
            
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if i >= len(nums):
                break

            target = -1 * nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    output.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < len(nums) and right > i and nums[left] == nums[left - 1] and nums[right] == nums[right + 1]:
                        left += 1
                        right -= 1
        return output

# nums=[-4,-1,-1,0,1,2]


