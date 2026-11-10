class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        
        def dfs(current_combination, total, number_index):            
            if total == target:
                output.append(current_combination.copy())
                return

            for i in range(number_index, len(nums)):
                if total + nums[i] > target:
                    return

                current_combination.append(nums[i])
                dfs(current_combination, total + nums[i], i)
                current_combination.pop()

        dfs([], 0, 0)
        return output

# time: O(nlogn) for sorting + O(n**t) for recursions * (O(t) for copying)  = O(t · nᵗ + nlogn)
# with n length of nums and t is the target, because all numbers are positive, so at most we will have 9 additions


# auxiliary space: O(t) for stack calls + O(t) for current combination list + O(n) for sorting = O(t + n) 
# output space: O(t*R) with R number of valid combinations 
# total space: O(t + n + t*R) = O(n + t +  t* R)
