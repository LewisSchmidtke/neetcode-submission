# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle with fast and slow 2pointer
        slow = head
        fast = head

        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of LL
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # iterate both sides to compare
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        
        return True
