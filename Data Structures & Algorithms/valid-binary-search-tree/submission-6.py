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
                new_min = curr_min
                new_max = curr.val

                dfs(curr.left, new_min, new_max)

            if curr.right:
                new_min = curr.val
                new_max = curr_max

                dfs(curr.right, new_min, new_max)
        
        # dfs(root, root.val, root.val)
        dfs(root, float('-inf'), float('inf'))

        return self.isBST


        