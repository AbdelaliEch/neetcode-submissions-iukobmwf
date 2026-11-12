# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = inorder_index = 0


        def dfs(limit):
            nonlocal preorder_index, inorder_index

            if preorder_index >= len(preorder):
                return None

            if inorder[inorder_index] == limit:
                inorder_index += 1
                return None
            
            
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            
            # root_inorder_index = (left_inorder_index + right_inorder_index) // 2

            # root.left = dfs(preorder_index + 1, left_inorder_index, root_inorder_index - 1)
            
            # preorder_index + (right_inorder_index - left_inorder_index)

            # # root.right = dfs(preorder_index + (right_inorder_index - left_inorder_index), root_inorder_index + 1, right_inorder_index)

            # root.right = dfs(preorder_index + root_inorder_index + 1, root_inorder_index + 1, right_inorder_index)

            return root
        
        return dfs(float('inf'))

        # return dfs(0, 0, len(preorder) - 1)

# 0 0 6
# 1 0 2
# 2 0 0
# 3 2 2
# 6 4 6
# 7 4 4
# 8 6 6




        # if not preorder or not inorder:
        #     return None
        
        # root = TreeNode(preorder[0])
        # root_inorder_index = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:root_inorder_index + 1], inorder[:root_inorder_index])
        # root.right = self.buildTree(preorder[root_inorder_index + 1:], inorder[root_inorder_index + 1:])

        # return root 




# [1 2 3 4 5 6 7]
# preorder = current node -> left subtree -> right subtree = 1 2 4 5 3 6 7
# inorder = left subtree -> current node -> right subtree = 4 2 5 1 6 3 7

# preorder always gives us the root node
# and the root is always at the middle of inorder, and everything to its left is left subtree, and vice versa for the right




# complexity is so big due to slicing and indexing, why not work with two pointers left and right
# time: O(n) for recursion calls * O()
# space: O(h)