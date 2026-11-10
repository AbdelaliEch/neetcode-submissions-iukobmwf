class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        current_path = []
        available_choices = ["take", "keep"]

        def dfs(depth):
            if depth == len(nums):
                output.append(current_path.copy())
                return

            for choice in available_choices:
                if choice == "take":
                    current_path.append(nums[depth])
                    dfs(depth + 1)
                    current_path.pop()
                else:
                    dfs(depth + 1)

        dfs(0)
        return output