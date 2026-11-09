# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resDummy = c3 = ListNode()

        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            c3.next = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10

            l1, l2, c3 = l1.next if l1 else None, l2.next if l2 else None, c3.next
        
        if carry:
            c3.next = ListNode(carry)

        return resDummy.next


# time: O(max(n, m))
# space: O(1)