# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.isBST = True

        def dfs(curr, curr_min, curr_max):
            if not curr or not self.isBST:
                return

            if curr.left and not (curr.left.val < curr.val and curr.left.val > curr_min):
                self.isBST = False
                return
            elif curr.right and not (curr.right.val > curr.val and curr.right.val < curr_max):
                self.isBST = False
                return

            if curr.left:
                dfs(curr.left, curr_min, curr.val)

            if curr.right:
                dfs(curr.right, curr.val, curr_max)
        
        dfs(root, float('-inf'), float('inf'))

        return self.isBST

# time: O()
# space: O()
        