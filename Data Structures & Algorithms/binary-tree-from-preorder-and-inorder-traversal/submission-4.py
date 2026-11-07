# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            root = TreeNode(root_val)
            root_inorder_idx = indices[root_val]


            root.left = dfs(l, root_inorder_idx - 1)
            root.right = dfs(root_inorder_idx + 1, r)

            return root

        return dfs(0, len(inorder) - 1)
        

# time: O(n) for creating the dict with n length of input arrays + amount of work time done per stack call
# space: O(n) for creating the dict with n length of input arrays + amount of work space used per stack call


# each call performs work time of: O(1) nothing done , so O(1) * n = O(n)
# so total time complexity is O(n) + O(n) = O(n)


# each call uses space time of: O(1) for creating the tree node, so O(1) * O(h) = O(h)
# so total space complexity is:  O(h) + O(n) = O(n)

