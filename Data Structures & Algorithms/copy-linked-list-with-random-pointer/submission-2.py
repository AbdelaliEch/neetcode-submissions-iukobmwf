"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copies = dict()
        res = c2 = Node(-1)

        c = head
        while c:
            c2.next = Node(c.val)
            c2 = c2.next
            original_to_copies[c] = c2
            c = c.next
        res = res.next

        for node in original_to_copies:
            copy_node = original_to_copies[node]
            node_random = node.random
            copy_node.random = original_to_copies[node_random] if node_random else None

        return res
