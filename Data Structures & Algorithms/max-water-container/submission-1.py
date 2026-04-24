class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        for l in range(len(heights) - 1):
            for r in range(l, len(heights)):
                amount = min(heights[l], heights[r]) * (r - l)
                max_amount = max(max_amount, amount)
        return max_amount   

# container amount is calculated by the surface, width * height

#time: O(n**2)
# space: O(1)