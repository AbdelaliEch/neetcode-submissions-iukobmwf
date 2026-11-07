# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.turns = 0
        self.res = None

        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.left)
            self.turns += 1
            # print(curr.val)
            if self.turns == k:
                # print("min", curr.val)
                self.res = curr.val
                # return curr.val
            dfs(curr.right)
            # return None
        
        dfs(root)
        return self.res
