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
        c1 = list1
        c2 = list2

        c3 = output
        while c1 and c2:
            if not c2 or c1.val <= c2.val:
                c3.val = c1.val
                c1 = c1.next
            else:
                c3.val = c2.val
                c2 = c2.next

            c3.next = ListNode()
            c3 = c3.next
        
        print(c3.val)

        if c2 and not c1:
            # print("c1 none", "c2 still", c2.val)
            c3.val = c2.val
            c2 = c2.next
            c3.next = c2    
        elif c1 and not c2:
            print("c2 none", "c1 still", c1.val)
            c3.val = c1.val
            c1 = c1.next
            c3.next = c1

        
        # c3 = c2 if not c1 else c1
        return output


# if not c1:
#     print("c1 none")
# if not c2:
#     print("c2 none")
# if c1 and c2:
#     print(c1.val, c2.val, c3.val)