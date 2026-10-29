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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        output = c3 = ListNode()
        carry = 0
        while c1 or c2:            
            val1 = c1.val if c1 else 0
            val2 = c2.val if c2 else 0

            total = val1 + val2 + carry
            carry = 0
            if total <= 9:
                c3.next = ListNode(total)
            else:
                c3.next = ListNode(total - 10)
                carry = 1

            
            c1 = c1.next if c1 else c1
            c2 = c2.next if c2 else c2
            c3 = c3.next
        
        if carry != 0:
            c3.next = ListNode(carry)
            
        return output.next
        
# time: O(m) with m max length of l1 and l2
# space: O(1) auxiliary space