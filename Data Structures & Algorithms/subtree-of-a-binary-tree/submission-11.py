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

# time: O(min(n, m))
# space: O(min(h1, h2))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subtreeFound = False

        def dfs(curr):
            if not curr:
                return
            
            nonlocal subtreeFound
            if self.isSameTree(curr, subRoot):
                subtreeFound = True
                return

            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return subtreeFound

# time: O(n * min(n, m)) with n number of tree given nodes and m number of subRoot tree nodes
# space: O(h1 + min(h1,h2))

