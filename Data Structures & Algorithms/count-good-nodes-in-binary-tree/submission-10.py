# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(curr, current_min):
            if not curr:
                return

            if curr.val >= current_min:
                self.count += 1
                current_min = curr.val
    
            dfs(curr.left, current_min)
            dfs(curr.right, current_min)

        
        dfs(root, float('-inf'))
        return self.count