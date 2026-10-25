class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start_index = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start_index = index
            stack.append((start_index, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

# time: O(n)
# space: O(n)

# 4 * (5 - 5 + 1) = 4
# 2 * (5 - 4 + 1) = 4
# 2 * (5 - 3 + 1) = 6



# 1 * (5 - 1 + 1) = 5

# 3 4 5 2 7 1
# [3 4 5]



# [7,1,7,2,2,4]
# 3(2)
# stack = [1(1) 2(7)]
          

# [1 2 3 4]


# first, what formes a rectangle
# so we can see all the rectangles possible
# will the largest rectangle contain the largest height
# starting from the left
# a rectangle between two bars: for example bar 0(7) and 1(1) is: min(height) * length = 1 * 