class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(current_combination, visited):
            if len(current_combination) == len(nums):
                output.append(current_combination.copy())
                return

            for num in nums:
                if num in visited:
                    continue
                
                current_combination.append(num)
                visited.add(num)

                dfs(current_combination, visited)

                current_combination.pop()
                visited.remove(num)

        dfs([], set())
        return output