class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # if not stack:
            #     stack.append((temp, i))
            # else:
            while stack and temp > stack[-1][0]:
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temp, i))
        return output
        



# it looks like we need a stack
# what will we push to the stack, when and when will we pop
# [30,38,30,36,35,40,28]