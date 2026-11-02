# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def reverse_list(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        c, length = head, 0
        while c:
            length += 1
            c = c.next
        
        c = head
        for _ in range(length // 2):
            c = c.next
        h2 = c.next
        c.next = None
        
        h2 = self.reverse_list(h2)

        c1, c2 = head, h2
        while c1 and c2:            
            n1, n2 = c1.next, c2.next

            c1.next = c2
            c2.next = n1

            c1 = n1
            c2 = n2
