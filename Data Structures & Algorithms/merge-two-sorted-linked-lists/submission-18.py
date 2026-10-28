# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = c3 = ListNode()
        c1, c2 = list1, list2
        while c1 and c2:
            if c1.val <= c2.val:
                c3.next = c1
                c1 = c1.next
                c3 = c3.next
                c3.next = None
            else:
                c3.next = c2
                c2 = c2.next
                c3 = c3.next
                c3.next = None
        c3.next = c2 if not c1 else c1
        return head.next

# time: O(n + m)
# space: O(1) auxiliary space