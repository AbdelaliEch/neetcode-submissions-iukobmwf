# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, root):
        if not root:
            return []
        
        output = []

        q = deque([root])

        while q:
            level = []
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(level)
        return output
        


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        print(self.bfs(root))
        levels = self.bfs(root)

        res = []
        for level in levels:
            res.append(level[-1])
        return res