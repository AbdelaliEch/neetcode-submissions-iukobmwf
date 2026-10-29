# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def print_list(self, head):
    #     c = head
    #     output = []
    #     while c:
    #         output.append(c.val)
    #         c = c.next
    #     return output

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        num1 = power1 = 0
        while c1:
            num1 += c1.val * pow(10, power1)
            power1 += 1
            c1 = c1.next

        c2 = l2
        num2 = power2 = 0
        while c2:
            num2 += c2.val * pow(10, power2)
            power2 += 1
            c2 = c2.next

        total = num1 + num2
        total_reversed = str(total)[::-1]

        output = c3 = ListNode()
        for digit in total_reversed:
            c3.next = ListNode(int(digit))
            c3 = c3.next
        return output.next

# time: O(m + n + k) with m length of l1, n length of l2 and k length of sum of numbers
# space: O(1) auxiliary space