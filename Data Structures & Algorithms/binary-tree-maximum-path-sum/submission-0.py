# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        # return max path sum without splitting from current node
        def dfs(curr):
            if not curr:
                return 0

            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # calculate max path sum if we split in current node
            self.res = max(self.res, leftMax + curr.val + rightMax)

            return curr.val + max(leftMax, rightMax)

        dfs(root)
        return self.res

# a valid path will consist of one split max
# split means taking both left and right children of a node
# in example 2: if we split on the root, we will start from 10 -> -15 -> 20, we can't split again at 20

# so we will start from the bottom and we will track what is the max without splitting and with splitting

# 