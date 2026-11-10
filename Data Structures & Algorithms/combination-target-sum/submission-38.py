class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()

        def dfs(curr_combination, total, number_index):
            if total == target:
                output.append(curr_combination.copy())
                return

            for i in range(number_index, len(nums)):
                if total + nums[i] > target:
                    return

                curr_combination.append(nums[i])
                dfs(curr_combination, total + nums[i], i)
                curr_combination.pop()
        
        dfs([], 0, 0)
        return output