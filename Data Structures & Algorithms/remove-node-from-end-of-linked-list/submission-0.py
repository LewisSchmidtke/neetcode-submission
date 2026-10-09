# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Remove from n-th position of end of the list
        dummy = ListNode(0, head)
        right = head
        left = dummy
        pos = 0

        while pos < n: # We move start of right pointer so that delta between right and left = n
            right = right.next
            pos += 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next # Skip the one we want to remove

        return dummy.next