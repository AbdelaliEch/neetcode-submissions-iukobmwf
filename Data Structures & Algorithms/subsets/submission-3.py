class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        current_path = []

        def dfs(depth):
            if depth == len(nums):
                output.append(current_path.copy())
                return

            
            current_path.append(nums[depth])
            dfs(depth + 1)
            current_path.pop()
            dfs(depth + 1)

        dfs(0)
        return output

# time: O(n * 2**n) with n length of nums, i.e depth of the decisions tree
# space: auxiliary space O(n), output space: O(n * 2**n), total space: O(n * 2**n)