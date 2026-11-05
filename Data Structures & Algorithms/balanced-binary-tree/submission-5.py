# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calculate_height(self, curr):
        if not curr:
            return 0
        
        left_height = self.calculate_height(curr.left) 
        right_height = self.calculate_height(curr.right)

        if left_height is False or right_height is False or abs(left_height - right_height) > 1:
            return False
        else:
            return 1 + max(left_height, right_height)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.calculate_height(root) is not False
       
        
# time: O(n)
# space: O(h) with h height of the tree
