# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        self.output = []
        self.count = 0

        def dfs(curr, curr_max):
            if not curr:
                return

            if curr.val >= curr_max:
                
                self.output.append(curr.val)
                self.count += 1

                curr_max = curr.val

            dfs(curr.left, curr_max)
            dfs(curr.right, curr_max)

        dfs(root, float('-inf'))
        # print(self.output, self.count)
        return self.count


# dfs