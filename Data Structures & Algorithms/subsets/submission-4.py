class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        def dfs(depth, current_combination):
            if depth == len(nums):
                output.append(current_combination.copy())
                return

            current_combination.append(nums[depth])
            dfs(depth + 1, current_combination)
            current_combination.pop()
            dfs(depth + 1, current_combination)

        dfs(0, [])
        return output