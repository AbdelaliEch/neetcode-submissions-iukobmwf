class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            # print(i, stack, output)
            if not stack or temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    # print("inside loop", i, stack, output)
                    output[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            # print(i, stack, output)
            # print()
        return output
# [30,38,30,36,35,40,28]
# stack = [1]  
# 1 0 1 0 0 0 0

