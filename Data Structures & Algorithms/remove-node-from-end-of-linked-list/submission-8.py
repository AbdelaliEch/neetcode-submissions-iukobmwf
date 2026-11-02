# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c, length = head, 0
        while c:
            length += 1
            c = c.next
        
        idx = length - n
        
        if length == 1:
            return None
        if n == length:
            return head.next

        c = head
        for _ in range(idx - 1):
            c = c.next
        c.next = c.next.next
        return head
            