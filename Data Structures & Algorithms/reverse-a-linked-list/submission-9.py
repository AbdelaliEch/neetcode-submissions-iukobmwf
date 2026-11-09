# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_list(self, head):
            c = head
            output = []
            while c:
                output.append(c.val)
                c = c.next
            return output
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head


        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev 
