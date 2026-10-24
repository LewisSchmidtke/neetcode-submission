# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        prev = None
        curr = head
        while curr:
            values.append(curr.val)

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = prev
        idx = 0
        while curr:
            if curr.val != values[idx]:
                return False
            idx += 1
            curr = curr.next
        
        return True



        