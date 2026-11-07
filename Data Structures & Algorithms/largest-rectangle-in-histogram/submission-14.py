class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            last_index = i
            while stack and h < stack[-1][1]:
                j, h2 = stack.pop()
                max_area = max(max_area, (i - j) * h2)
                last_index = j
            stack.append((last_index, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area

