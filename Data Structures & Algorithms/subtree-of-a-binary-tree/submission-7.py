# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtreeFound = False

        def dfs(curr):
            nonlocal subtreeFound, subRoot
            
            if subtreeFound or not curr:
                return

            if self.isSameTree(curr, subRoot):
                subtreeFound = True
                return
            else:
                dfs(curr.left)
                dfs(curr.right)

        dfs(root)
        return subtreeFound