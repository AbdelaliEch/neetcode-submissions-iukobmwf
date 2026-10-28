# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_list(self, list1: Optional[ListNode]):
        c = list1
        output = []
        if not c:
            return []
        while c:
            output.append(c.val)
            c = c.next
        return output

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if not list1 and not list2:
        #     return None
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return None

        first_node = True
        head = c3 = None
        c1, c2 = list1, list2
        while c1 and c2:
            print(self.print_list(c1), self.print_list(c2), self.print_list(c3), self.print_list(head))

            if not c2 or c1.val <= c2.val:
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

        print(self.print_list(c1), self.print_list(c2), self.print_list(c3), self.print_list(head))
        
        c3.next = c2 if not c1 else c1

        print(self.print_list(c1), self.print_list(c2), self.print_list(c3), self.print_list(head))

        return head
        # if c2 and not c1:
        #     c3.val = c2.val
        #     c2 = c2.next
        #     c3.next = c2    
        # elif c1 and not c2:
        #     c3.val = c1.val
        #     c1 = c1.next
        #     c3.next = c1

        # return output

# time: O(n + m)
# space: O(m + n) because of creating new nodes