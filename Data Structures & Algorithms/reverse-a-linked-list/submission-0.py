# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        c = head
        while c != None:
            lst.append(c.val)
            c = c.next
        
        lst = lst[::-1]

        c = head
        for i in range(len(lst)):
            c.val = lst[i]
            c = c.next
        
        return head