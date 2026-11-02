# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyRes = c = ListNode()
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            print(val1, val2, carry)

            total = (val1 + val2 + carry)
            resVal = total % 10
            carry = total // 10
            
            c.next = ListNode(resVal)
            c = c.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        c.next = ListNode(carry) if carry else None

        return dummyRes.next