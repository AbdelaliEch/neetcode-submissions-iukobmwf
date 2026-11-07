# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        self.count = 0
        curr_max = float("-inf")
        def dfs(curr):
            nonlocal curr_max
            if not curr:
                return

            if curr.val >= curr_max:                
                self.count += 1
                curr_max = curr.val
            tmp = curr_max
            dfs(curr.left)   
            curr_max = tmp
            dfs(curr.right)

        dfs(root)
        return self.count


# dfs