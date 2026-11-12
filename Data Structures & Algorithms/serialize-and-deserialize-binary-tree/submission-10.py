# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        lst = []
        def dfs(curr):
            if not curr:
                lst.append("N")
                return  

            lst.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)
        
        dfs(root)
        return ",".join(lst)

# time: O(n)
# space: O(n)
  
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        data = data.split(",")
        self.data_index = 0

        def dfs():
            if self.data_index == len(data):
                return None

            if data[self.data_index] == "N":
                self.data_index += 1
                return None


            curr = TreeNode(int(data[self.data_index]))
            self.data_index += 1
            
            curr.left = dfs()
            curr.right = dfs()

            return curr

        return dfs()

# time: O(n)
# space: O(n)

# 12NN34NN5NN



# we need to serialize as we deserialize, so let's use preorder dfs
# preorder = current node -> left subtree -> right subtree


# or maybe BFS?????????/