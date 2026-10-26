class Solution:
    def trap(self, height: List[int]) -> int:
        max_right_borders = [0] * len(height)
        max_left_borders = [0] * len(height)

        current_left_max = current_right_max = 0
        for i in range(len(height)):
            max_left_borders[i] = current_left_max
            current_left_max = max(current_left_max, height[i])

        for i in range(len(height) - 1, -1, -1):
            max_right_borders[i] = current_right_max
            current_right_max = max(current_right_max, height[i])
        output = 0
        for i, h in enumerate(height):
            output += max(min(max_left_borders[i], max_right_borders[i]) - h, 0) 
        return output

# time: O(n)
# space: O(n)

# instead of thinking between bars, think about how much water will get trapped in each bar
# for each bar, the amount of water that will get trapped in it depends on its borders
# for first and last bar, one of their borders is missing, so 0 trapped water

# for bar number 5, the amount of trapped water innit is 3, why?
# because it has two borders with height 3

# for bar number 2, the amount of trapped water innit is 2, why?
# because it has two borders, one with height 2 and one with height 3, so the min between its borders

# for bar number 4, the amount of trapped water innit is 2, why?
# because it has two borders with height 3, but its own height is 1, so 3 - 1 = 2

# btw not any border, the max border to the right and the max border to the left


# so first task is to determine the max border to the right and to the left for each bar
