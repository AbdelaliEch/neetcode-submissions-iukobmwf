# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resDummy = c3 = ListNode()

        c1, c2 = l1, l2
        carry = 0
        while c1 or c2:
            # print(c1.val, c2.val)
            val1 = c1.val if c1 else 0
            val2 = c2.val if c2 else 0

            c3.next = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10

            c1, c2, c3 = c1.next if c1 else None, c2.next if c2 else None, c3.next
        if carry:
            c3.next = ListNode(carry)

        return resDummy.next


# 999999
# +
#    999
# =
#         

# 28

# 28 / 10 = 2

# 28 % 10 = 