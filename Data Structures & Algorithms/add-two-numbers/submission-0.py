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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        num1 = power1 = 0
        while c1:
            num1 += c1.val * pow(10, power1)
            power1 += 1
            c1 = c1.next
        print(num1)

        c2 = l2
        num2 = power2 = 0
        while c2:
            num2 += c2.val * pow(10, power2)
            power2 += 1
            c2 = c2.next
        print(num2)

        total = num1 + num2
        print(total)

        total_reversed = str(total)[::-1]

        output = c3 = ListNode()
        for digit in total_reversed:
            c3.next = ListNode(digit)
            c3 = c3.next
        print(self.print_list(output))
        return output.next




        # c1, c2, c3 = l1, l2, output
        # while c1 and c2:
        #     print(self.print_list(c1), self.print_list(c2), self.print_list(output))
        #     c3.next = ListNode(c1.val + c2.val)
        #     c3 = c3.next
        #     c1 = c1.next
        #     c2 = c2.next
        # # c3.next = ListNode(c1.val + c2.val)
        # print(self.print_list(c1), self.print_list(c2), self.print_list(output))
        # return output.next
