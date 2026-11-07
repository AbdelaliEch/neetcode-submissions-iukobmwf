class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            # print('outside', stack)
            last_index = i
            while stack and h < stack[-1][1]:
                # print('inside', stack, max_area)
                j, h2 = stack.pop()
                # print((j - i) * h2)
                max_area = max(max_area, (i - j) * h2)
                last_index = j
            stack.append((last_index, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        # print(stack)
        return max_area

            # if not stack or h > stack[-1][1]:
                # stack.append((i, h))
