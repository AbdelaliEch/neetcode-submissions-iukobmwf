class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                j = stack.pop()[0]
                output[j] = i - j
            stack.append((i, temp))
        return output

# time: O(n)
# space: O(n)
            