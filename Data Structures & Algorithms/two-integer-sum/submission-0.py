class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in my_dict:
                return [my_dict[difference], i]
            else:
                my_dict[nums[i]] = i