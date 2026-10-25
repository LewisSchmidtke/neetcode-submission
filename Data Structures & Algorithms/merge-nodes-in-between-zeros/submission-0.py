# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = traverse = head
        curr = head.next
        count = 0
        while curr:
            if curr.val != 0:
                count += curr.val
            else:
                curr.val = count
                count = 0
                traverse.next = curr
                traverse = curr
            
            curr = curr.next

        return dummy.next