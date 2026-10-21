class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
        return output

# time: O(n**2)
# space: O(1)

