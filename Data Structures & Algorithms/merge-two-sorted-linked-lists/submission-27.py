# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_list(self, head):
        c = head
        output = []
        while c:
            output.append(c.val)
            c = c.next
        return output


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyRes = c = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            c = c.next
        
        c.next = list1 if list1 else list2
        
        print(self.print_list(list1), self.print_list(list2), self.print_list(dummyRes))

        return dummyRes.next