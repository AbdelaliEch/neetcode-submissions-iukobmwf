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
            # if curr:
            #     print(curr.val, self.order)
            # else:
            #     print(None, self.order)

            if not curr or self.res:
                return
        

            # if self.order == k:
            #     self.res = curr.val

            dfs(curr.left)
            
            self.order += 1

            if self.order == k:
                self.res = curr.val

            dfs(curr.right)

        dfs(root)
        return self.res
        

# inorder = left subtree -> current node -> right subtree = [3 5 6 7]
