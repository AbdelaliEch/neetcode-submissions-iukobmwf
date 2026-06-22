# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
    
        c1, c2 = list1, list2

        if c1.val <= c2.val:
            newList = ListNode(c1.val)
            c1 = c1.next
        else:
            newList = ListNode(c2.val)
            c2 = c2.next

        c3 = newList
        while c1 and c2:   
            if c1.val <= c2.val:
                c3.next = ListNode(c1.val)
                c1 = c1.next
            else:
                c3.next = ListNode(c2.val)
                c2 = c2.next
            c3 = c3.next
            print()
        
        c3.next = c1 if c1 else c2
        return newList
        
            