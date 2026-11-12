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
            
            # print(curr.val, current_max, current_min)

            if curr.left and not(curr.left.val < curr.val and curr.left.val > current_min):
                self.isValid = False
                return

            if curr.right and not (curr.right.val > curr.val and curr.right.val < current_max):
                self.isValid = False
                return

            # new_min = curr.val
            new_min = current_min
            new_max = curr.val

            dfs(curr.left, new_max, new_min)

            new_min = curr.val
            new_max = current_max
            dfs(curr.right, new_max, new_min)

        dfs(root, float('inf'), float('-inf'))
        return self.isValid