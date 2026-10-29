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
        
        index = length - n
        print(length, n, index)

        if index < 1:
            return head.next


        c = head
        for i in range(index - 1):
            c = c.next
        
        prev_node = c
        to_remove = c.next
        next_node = c.next.next
        
        # print(c.val)
        # print(prev_node.val)
        # print(to_remove.val)
        # print(next_node.val)

        prev_node.next = next_node

        return head

    

