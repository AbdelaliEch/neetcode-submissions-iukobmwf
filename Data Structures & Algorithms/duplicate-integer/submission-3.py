class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_set = set(nums)
        return len(s_set) != len(nums)
        