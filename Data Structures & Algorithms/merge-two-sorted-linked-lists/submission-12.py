# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        output = ListNode()
        c1, c2, c3 = list1, list2, output
        while c1 and c2:
            if not c2 or c1.val <= c2.val:
                c3.val = c1.val
                c1 = c1.next
            else:
                c3.val = c2.val
                c2 = c2.next
            c3.next = ListNode()
            c3 = c3.next
        
        if c2 and not c1:
            c3.val = c2.val
            c2 = c2.next
            c3.next = c2    
        elif c1 and not c2:
            c3.val = c1.val
            c1 = c1.next
            c3.next = c1

        return output


# if not c1:
#     print("c1 none")
# if not c2:
#     print("c2 none")
# if c1 and c2:
#     print(c1.val, c2.val, c3.val)