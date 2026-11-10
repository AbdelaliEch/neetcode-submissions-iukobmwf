class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        current_combination = []

        def dfs(current_combination, nums):
            current_total = sum(current_combination)

            if current_total > target:
                return

            if current_total == target:
                output.append(current_combination.copy())
                return

            # print("current combination", current_combination, "current nums", nums)
            for i, num in enumerate(nums):
                current_combination.append(num)
                dfs(current_combination, nums[i:])
                current_combination.pop()

        dfs(current_combination, nums)
        return output
