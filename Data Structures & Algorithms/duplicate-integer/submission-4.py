class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = len(set(nums))
        return s != n
        