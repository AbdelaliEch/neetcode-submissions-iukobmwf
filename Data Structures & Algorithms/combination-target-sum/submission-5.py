class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        output = []

        current_combination, current_total = [], 0

        def dfs(current_total):
            if current_total > target:
                return

            if current_total == target:
                output.append(current_combination.copy())
                return

            for i, num in enumerate(nums):
                if not current_combination or num >= current_combination[-1]:    
                    current_combination.append(num)
                    current_total += num

                    dfs(current_total)

                    current_combination.pop()
                    current_total -= num

        dfs(current_total)
        return output

# time: O(nlogn) for sorting + O(n**t) for recursions * (O(t) for copying)  = O(t · nᵗ + nlogn)
# with n length of nums and t is the target, because all numbers are positive, so at most we will have 9 additions


# auxiliary space: O(t) for stack calls + O(t) for current combination list + O(n) for sorting = O(t + n) 
# output space: O(t*R) with R number of valid combinations 
# total space: O(t + n + t*R) = O(n + t +  t* R)
