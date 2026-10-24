class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_amount = 0
        while left < right:
            amount = (right - left) * min(heights[left], heights[right])
            max_amount = max(max_amount, amount)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1 
        return max_amount