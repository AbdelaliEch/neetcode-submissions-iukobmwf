class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        output = []
        for i in range(len(nums)):
            # to stop at positive numbers
            if nums[i] > 0:
                break
            # to avoid same target
            # while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
            #     i += 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # check if i still inside range
            if i >= len(nums):
                break

            # set target
            target = -1 * nums[i]

            # set the two pointers
            left = i + 1
            right = len(nums) - 1

            # start sorted two sum
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                # found equality
                else:
                    # append triplets
                    output.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < len(nums) and right > i and nums[left] == nums[left - 1] and nums[right] == nums[right + 1]:
                        left += 1
                        right -= 1
        return output

# nums=[-4,-1,-1,0,1,2]


