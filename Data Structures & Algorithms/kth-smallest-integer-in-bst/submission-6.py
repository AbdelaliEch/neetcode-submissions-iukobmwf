# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.order = 0
        self.res = None

        def dfs(curr):
            if not curr or self.res:
                return
        
            dfs(curr.left)
            
            self.order += 1
            if self.order == k:
                self.res = curr.val
                return
            dfs(curr.right)

        dfs(root)
        return self.res
        
# time: O(n)
# space: O(h)

# inorder = left subtree -> current node -> right subtree
