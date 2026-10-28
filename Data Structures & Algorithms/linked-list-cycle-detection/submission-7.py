# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c = head
        visited = set()
        while c:
            if c in visited:
                return True
            visited.add(c)
            c = c.next
        return False
