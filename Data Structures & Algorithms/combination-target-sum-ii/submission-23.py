class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def dfs(curr_combination, total, number_index):
            if total == target:
                output.append(curr_combination.copy())
                return


            for i in range(number_index, len(candidates)):
                if i > number_index and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    return

                curr_combination.append(candidates[i])
                dfs(curr_combination, total + candidates[i], i + 1)
                curr_combination.pop()
        
        dfs([], 0, 0)

        return output


# if we are still inside the same dfs function, that means we are still inside the same recursion level , i.e dfs call
# we need to prevent duplicates there?

# i need to skip duplicates horizontally not vertically
