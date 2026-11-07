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
            if not curr or self.res:
                return
            
            dfs(curr.left)
            self.turns += 1
            if self.turns == k:
                self.res = curr.val
            dfs(curr.right)
        
        dfs(root)
        return self.res

# time: O()
# space: O()
