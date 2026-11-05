# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0

        def calculate_height(curr):
            if not curr:
                return 0

            left_height = calculate_height(curr.left)
            right_height = calculate_height(curr.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        calculate_height(root)
        return self.diameter
        
        




# max diameter is the max left + right heights, we need to move through each node and calculate its right and left height and sum them and compare it to the current found
# diameter