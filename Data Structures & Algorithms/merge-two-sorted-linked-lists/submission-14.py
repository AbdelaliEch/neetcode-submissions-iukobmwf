# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        first_node = True
        head = c3 = None
        c1, c2 = list1, list2
        while c1 and c2:
            if c1.val <= c2.val:
                if first_node:
                    head = c3 = c1
                    c1 = c1.next
                    c3.next = None 
                    first_node = False
                else:
                    c3.next = c1
                    c1 = c1.next
                    c3 = c3.next
                    c3.next = None
            else:
                if first_node:
                    head = c3 = c2 
                    c2 = c2.next
                    c3.next = None
                    first_node = False
                else:
                    c3.next = c2
                    c2 = c2.next
                    c3 = c3.next
                    c3.next = None
        c3.next = c2 if not c1 else c1
        return head

# time: O(n + m)
# space: O(1) auxiliary space