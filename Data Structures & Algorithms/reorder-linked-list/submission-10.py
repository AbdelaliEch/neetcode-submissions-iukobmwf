# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_list(self,head):
        c = head
        output = []
        while c:
            output.append(c.val)
            c = c.next
        return output
    
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
        
        print(self.print_list(head), self.print_list(h2))
        h2 = self.reverse_list(h2)
        print(self.print_list(head), self.print_list(h2))


        c1, c2 = head, h2
        while c1 and c2:
            print(self.print_list(c1), self.print_list(c2), self.print_list(head))
            
            n1, n2 = c1.next, c2.next

            c1.next = c2
            c2.next = n1

            c1 = n1
            c2 = n2
            
            # c3.next = c1
            # c1 = n1

            # c3 = c3.next

            # c3.next = c2
            # c2 = n2
        
        # head = output.next





