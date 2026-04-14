# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        
        lst1 = []
        lst2 = []
        c1 = list1
        c2 = list2
        while c1:
            lst1.append(c1.val)
            c1 = c1.next
        while c2:
            lst2.append(c2.val)
            c2 = c2.next
        
        result = sorted(lst1 + lst2)
        list3 = ListNode()
        c3 = list3
    
        for i in range(len(result)):
            c3.val = result[i]
            if i != len(result) - 1:
                c3.next = ListNode()
                c3 = c3.next

        

        return list3