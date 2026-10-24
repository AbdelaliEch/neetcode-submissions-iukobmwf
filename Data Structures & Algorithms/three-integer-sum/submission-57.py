class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        output = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = nums[i] * -1
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                # print(nums[i], nums[left], nums[right])
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    # print("appended")
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return output

# time: O(n**2)
# space: O(n) if we count the sorting space


# [-4, -1, -1, 0, 1, 2]
# nums[i] + nums[j] + nums[k] == 0     <=>   nums[j] + nums[k] == - nums[i] 
