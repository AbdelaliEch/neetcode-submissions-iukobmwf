class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_height = [0] * len(height)
        current_left_max = 0
        for i in range(len(height)):
            max_left_height[i] = current_left_max
            current_left_max = max(current_left_max, height[i])

        max_right_height = [0] * len(height)
        current_right_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_right_height[i] = current_right_max
            current_right_max = max(current_right_max, height[i])
  
        count = 0
        for i in range(len(height)):
            trapped_water = min(max_left_height[i], max_right_height[i]) - height[i]
            count += max(trapped_water, 0)
        return count

# time: O(n)
# space: O(n)



# we need to count the amount of water trapped in each position
# for example in position 5, the amount of water trapped is 3, why is that?
# because it has a bar with height 3 on the left, and another one with same height on the right, and its height is 0
# so for each position we need to find the highest bar to the left and to the right and do : min(left, right) - height[i]