# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=None, next=head)
        prev, curr = dummy, head

        while curr:
            if prev.val is None:
                prev = curr
                curr = curr.next
                continue

            if curr.val != prev.val:
                prev = curr
            else:
                prev.next = curr.next 
            
            curr = curr.next
        
        return dummy.next
