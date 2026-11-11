class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        def dfs(depth, current_combination):
            if depth == len(nums):
                output.append(current_combination.copy())
                return

            # if depth + 1 < len(nums) and nums[depth] == nums[depth + 1]:
            #     output.append(current_combination.copy())


            # first iteration: add current depth's number
            current_combination.append(nums[depth])
            dfs(depth + 1, current_combination)
            current_combination.pop()
            
            skip_depth = depth
            while skip_depth + 1 < len(nums) and nums[skip_depth] == nums[skip_depth + 1]:
                skip_depth += 1
            # second iteration: skip current depth's number
            dfs(skip_depth + 1, current_combination)

        dfs(0, [])
        return output














# allow duplicates vertically but not horizontally
# we need to stop duplicates when we are inside same level, so horizontally

# horizontal = same dfs level
# vertical = different dfs level

# what if inside a level, if nums of current depth is similar to previous depth, then we don't do the skip part, we only use the 'add' choice