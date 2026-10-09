# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current2 = l2
        current1 = l1
        carry_one = 0

        while current2:
            temp_current2 = current2.val
            temp_current1 = current1.val
            result = temp_current2 + temp_current1 + carry_one

            if result < 10:
                current2.val = result
            else:
                carry_one = 1
                current2.val = result - 10

            if current2.next is None:
                break

            current2 = current2.next
            current1 = current1.next

        if carry_one > 0:
            last_node = ListNode(1, None)
            current2.next = last_node

        return l2
        
