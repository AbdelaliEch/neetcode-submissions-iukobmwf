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

        if length == 1:
            return None
        elif n == length:
            return head.next 

        c, index = head, length - n
        for i in range(index - 1):
            c = c.next
        
        # prev_node = c
        # to_remove = c.next
        # next_node = c.next.next

        c.next = c.next.next

        return head

    

