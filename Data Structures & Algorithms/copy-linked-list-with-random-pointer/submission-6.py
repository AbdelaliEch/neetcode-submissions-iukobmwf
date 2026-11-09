"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def print_list(self, head):
            c = head
            output = []
            while c:
                output.append(c.val)
                c = c.next
            return output

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        c = head
        original_to_copies = dict()

        while c:
            original_to_copies[c] = Node(c.val)
            c = c.next

        c = head
        while c:
            original_to_copies[c].next = original_to_copies[c.next] if c.next else None
            original_to_copies[c].random = original_to_copies[c.random] if c.random else None
            c = c.next

        return original_to_copies[head]