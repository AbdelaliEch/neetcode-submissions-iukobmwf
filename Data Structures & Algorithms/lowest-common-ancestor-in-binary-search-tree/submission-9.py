# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # res = root

        # def dfs(curr):
        #     if not curr:
        #         return

        #     nonlocal p, q, res
   
        #     if curr.val >= p.val and curr.val >= q.val:
        #         print('entered here to go left', curr.val, p.val, q.val)
        #         dfs(curr.left)
        #     elif curr.val <= p.val and curr.val <= q.val:
        #         print('entered here to go right', curr.val, p.val, q.val)
        #         dfs(curr.right)
        #     else:
        #         print('entered here to update res', curr.val, p.val, q.val)
        #         res = curr


        curr = root

        while curr not in (p, q):
            if curr.val >= p.val and curr.val >= q.val:
                print('entered here to go left', curr.val, p.val, q.val)
                curr = curr.left
            elif curr.val <= p.val and curr.val <= q.val:
                print('entered here to go right', curr.val, p.val, q.val)
                curr = curr.right
            else:
                print('entered here to update res', curr.val, p.val, q.val)
                return curr
                # res = curr

        # dfs(root)
        return curr
             
#   2
# 1

# LCA 
# dfs
