# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.preorder_idx = 0

        def dfs(inorder_l_idx, inorder_r_idx):
            if inorder_l_idx > inorder_r_idx:
                return None
            
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            self.preorder_idx += 1
            
            root_inorder_idx = indices[root_val]
            
            root.left = dfs(inorder_l_idx, root_inorder_idx - 1)
            root.right = dfs(root_inorder_idx + 1, inorder_r_idx)

            return root

        return dfs(0, len(inorder) - 1)

# time: O(n)
# space: O(n)

# preorder = [1,2,3,4], 
# inorder = [2,1,3,4] 

# preorder gives us current node, inorder gives us what on the left of this node and what is on the right
# but we need to know where current node is in inorder, because its not always in the middle

# preorder = current node -> left subtree -> right subtree
# inorder = left subtree -> current node -> right subtree


