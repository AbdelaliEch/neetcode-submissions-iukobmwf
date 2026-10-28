class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while stack and h < stack[-1][1]:
                    index, height = stack.pop()
                    max_area = max(max_area, height * (i - index))
                stack.append((index, h))
        # print(stack)
        
        for i, h in stack:
            area = h * (len(heights) - i)
            # print(i, h, area)
            max_area = max(max_area, h * (len(heights) - i))
        return max_area



# for each bar, we need to see how much we can extend each height/bar

# we need to store and calculate how far a bar can be extended

# for bar 7, it can't be extended longer , because the bar next to it is smaller : 1 < 7