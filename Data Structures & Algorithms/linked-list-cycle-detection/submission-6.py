# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c1 = head
        if not head:
            return False
        c2 = head.next

        while c1 and c2 and c2.next:
            if c1 is c2:
                return True
            c1 = c1.next
            c2 = c2.next.next
        return False

# complexity: O(N) o(1)