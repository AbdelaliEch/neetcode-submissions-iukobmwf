# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
    
        self.preorderIndex = 0

        def dfs(l, r):
            if l > r:
                return None


            root_val = preorder[self.preorderIndex]
            self.preorderIndex += 1
            root = TreeNode(root_val)
            root_inorder_index = indices[root_val]

            root.left = dfs(l, root_inorder_index - 1)
            root.right = dfs(root_inorder_index + 1, r)

            return root

        return dfs(0, len(inorder) - 1) 

# time: O(n)
# space: O(n)



# [1 2 3 4 5 6 7]
# preorder = current node -> left subtree -> right subtree = 1 2 4 5 3 6 7
# inorder = left subtree -> current node -> right subtree = 4 2 5 1 6 3 7

# preorder always gives us the root node
# and the root is always at the middle of inorder, and everything to its left is left subtree, and vice versa for the right