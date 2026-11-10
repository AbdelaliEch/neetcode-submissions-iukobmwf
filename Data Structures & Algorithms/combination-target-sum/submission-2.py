class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        current_combination, current_total = [], 0

        def dfs(current_total, nums):
            # current_total = sum(current_combination)

            if current_total > target:
                return

            if current_total == target:
                output.append(current_combination.copy())
                return

            for i, num in enumerate(nums):
                current_combination.append(num)
                current_total += num

                dfs(current_total, nums[i:])

                current_combination.pop()
                current_total -= num

        dfs(current_total, nums)
        return output

# time: O(n**t) for recursions * (O(t) for sum work + O(t) for copying + O(n) for slicing nums) = O((n+t)*n**t) 
# with n length of nums and t is the target, because all numbers are positive, so at most we will have 9 additions


# auxiliary space: O(t) for stack calls + O(t) for current combination list + O(t * n) for slicing (max memory occupied at the same time) 
# = O(t * n)
# output space: O(t*R) with R number of valid combinations 
# total space: O(t*R + t*n) = O(t * (R + n))


# slicing + sum are expensive
