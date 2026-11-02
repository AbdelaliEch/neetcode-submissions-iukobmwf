class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        max_right_borders = [0] * len(height)
        max_left_borders = [0] * len(height)

        max_right = max_left = 0
        for i in range(len(height)):
            max_left_borders[i] = max_left
            max_left = max(max_left, height[i])
        for i in range(len(height) - 1, -1, -1):
            max_right_borders[i] = max_right
            max_right = max(max_right, height[i])

        for i in range(len(height)):
            res += max(min(max_right_borders[i], max_left_borders[i]) - height[i], 0)

        return res

# time: O(n)
# space: O(n)