# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        isBalanced = True
        
        def dfs(curr):
            nonlocal isBalanced

            if not curr:
                return 0

            left_height = dfs(curr.left)
            right_height = dfs(curr.right)

            if abs(left_height - right_height) > 1:
                isBalanced = False

            return 1 + max(left_height, right_height)

        dfs(root)
        return isBalanced

# dfs