class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                last_temp, last_index = stack.pop()
                result[last_index] = i - last_index
            stack.append((temp, i))
            
        return result

# time: O(n)
# space:  O(n) 