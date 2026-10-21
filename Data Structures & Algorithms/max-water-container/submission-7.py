class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            amount = min(heights[left], heights[right]) * (right - left)
            max_amount = max(max_amount, amount)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_amount


# time: O(n)
# space: O(1)

# [1,7,2,5,4,7,3,6]
# amount = height * length = min_height * diff_between_bars