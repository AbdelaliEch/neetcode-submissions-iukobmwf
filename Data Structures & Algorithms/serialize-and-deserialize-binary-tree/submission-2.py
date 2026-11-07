# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preorder
        res = []
        def dfs(curr):
            if not curr:
                res.append("N")
            else:
                res.append(str(curr.val))
                dfs(curr.left)
                dfs(curr.right)        
        dfs(root)
        return ",".join(res)


# time: O(n)
# space: O(h) + O(n) = O(n)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = data.split(",")
        idx = 0

        def dfs():
            nonlocal idx
            if lst[idx] == "N":
                idx += 1
                return
            
            node = TreeNode(int(lst[idx]))
            
            idx += 1
            
            node.left = dfs()
            node.right = dfs()
            
            return node

        return dfs()

# time: O(n)
# space: O(h) + O(n) = O(n)
