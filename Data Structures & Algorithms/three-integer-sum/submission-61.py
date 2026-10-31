class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        # print(nums)
        
        for i in range(len(nums)):
            # print("i", i)
            if nums[i] > 0:
                return output
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i] * -1
            left, right = i + 1, len(nums) - 1
            while left < right:
                # print(i, target, nums[left], nums[right])
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    # print("appended")
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    # print("left right", left, right)
        return output


            
