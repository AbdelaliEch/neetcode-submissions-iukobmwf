class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        
        for i, num in enumerate(nums):
            if target - num not in my_dict:
                my_dict[num] = i
            else:
                return [my_dict[target - num], i]

# time: O(n)
# space: O(n)
