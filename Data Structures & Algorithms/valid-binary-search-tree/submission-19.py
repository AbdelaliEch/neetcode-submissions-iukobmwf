# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True

        def dfs(curr, current_max, current_min):
            if not self.isValid:
                return
            if not curr:
                return
            

            if curr.left and not(curr.left.val < curr.val and curr.left.val > current_min):
                self.isValid = False
                return

            if curr.right and not (curr.right.val > curr.val and curr.right.val < current_max):
                self.isValid = False
                return

            dfs(curr.left, curr.val, current_min)
            dfs(curr.right, current_max, curr.val)

        dfs(root, float('inf'), float('-inf'))
        return self.isValid